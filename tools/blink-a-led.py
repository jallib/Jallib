#!/usr/bin/python3
""" Create and compile blink-a-led samples.

  Author: Rob Hamerling, Copyright (c) 2008..2017, all rights reserved.

  Adapted-by: Rob Jansen, Copyright (c) 2018..2022, all rights reserved.

  Revision: $Revision$

  Compiler: N/A

  This file is part of jallib  https://github.com/jallib/jallib
  Released under the ZLIB license
                 http://www.opensource.org/licenses/zlib-license.html

  Description: Python script to create blink-a-led samples
               for every available device file.
               - Validate the device file
               - Create a sample program
               - Validate the sample program
               - Compile the sample program
               - Check the compiler output for errors and warnings
               When all OK:
               - in PROD mode move the source of the sample to
                 the jalLib sample directory
               - in TEST mode move the source to ./test

  Sources:

  Version: 0.6

  Notes:
   - A blink-a-led sample is generated for every device file:
     a HS sample if possible and INTOSC sample if possible
   - For all PICs with USB support a sample is generated using HS_USB.
   - With a second commandline argument the generation of samples can be
     limited to a subset: specify a PICname (with wildcard characters).

"""

from pic2jal_environment import check_and_set_environment
base, mplabxversion = check_and_set_environment()    # obtain environment variables
if (base == ""):
   exit(1)

import sys
import os
import datetime
import time
import glob
import subprocess
import shutil
import json
import platform

platform_name = platform.system()

# --- general constants

ScriptAuthor    = "Rob Hamerling, Rob Jansen"
CompilerVersion = "2.5r6"


# specification of system dependent compiler executable
if (platform_name == "Linux"):
   compiler = os.path.join(os.getcwd(), "jalv2-x86-64")
elif (platform_name == "Windows"):
   compiler = os.path.join(os.getcwd(), "jalv2.exe")
elif (platform_name == "Darwin"):
   compiler = os.path.join(os.getcwd(), "jalv2osx")
else:
   print("Please specify platform specific compiler to this script!")

devdir = os.path.join(base, "test")                      # device files
dstdir = os.path.join(base, "blink")                     # destination of samples
if (not os.path.exists(dstdir)):
   os.makedirs(dstdir)

# Name of python executable is required for calling the jallib script.
python_exec = "python3"                                  # assume python2 and python3 are installed
try:
   log = subprocess.check_output([python_exec, "--version"], shell=False)
except:
   python_exec = "python"                                # Python3 is probably default

devspecfile = os.path.join(base, "devicespecific.json")  # some PIC properties needed here.


# global dictionaries for PIC information, re-filled with every PIC
var = {}
fusedef = {}
devspec = {}  # contents of devicespecific.json

# -----------------------------------------------------------
def collect_fusedef(fp):
   """ Scan (part of) device file for keywords of current fusedef
       This procedure is called from scan_devfile() and:
       - assumes the devicefile is opened
       - starts reading from the current location
   """
   kwdlist = []
   ln = fp.readline()
   while (ln != ""):
      words = ln.split()
      if (words[0] == "}"):                                    # end of this fusedef
         break
      kwdlist.append(words[0])
      ln = fp.readline()
   return kwdlist

def read_devspec_file():
    """ Read devicespecific.json

   Input:   (nothing, uses global variable 'devspec')
   Output:  fills "devspec" dictionary
   Returns: (nothing)
   """
    global devspec  # global variable
    with open(devspecfile, "r") as fp:
        devspec = json.load(fp)  # obtain contents devicespecific


# ------------------------------------------------------------
def scan_devfile(devfile):
   """ Scan device file for selected device info.
       Notes: - returns info in the exposed global variables.
   """
   global var
   var = {"ircfwidth" : 0}                                     # default width of OSCCON_IRCF
   global fusedef
   fusedef = {}                                                # clear (empty)
   fp = open(os.path.join(devdir,devfile), "r")
   ln = fp.readline()                                          # first line
   while (ln != ""):
      words = ln.split()
      if (len(words) == 0):
         pass
      elif (words[0] == "--"):
         pass
      elif (len(words) > 2):
         if ((words[0] == "pragma") & (words[1] == "fuse_def")):  # obtain fuse_def keyword if any
            fuse = words[2]
            if (fuse.startswith("BROWNOUT")):
               fusedef["brownout"] = collect_fusedef(fp)
            elif (fuse.startswith("CLKOUTEN")):
               fusedef["clkouten"] = collect_fusedef(fp)
            elif (fuse.startswith("CPUDIV")):
               fusedef["cpudiv"] = collect_fusedef(fp)
            elif (fuse.startswith("CSWEN")):
               fusedef["cswen"] = collect_fusedef(fp)
            elif (fuse.startswith("DEBUG")):
               fusedef["debug"] = collect_fusedef(fp)
            elif (fuse.startswith("FCMEN")):
               fusedef["fcmen"] = collect_fusedef(fp)
            elif (fuse.startswith("FOSC2")):
                fusedef["fosc2"] = collect_fusedef(fp)
            elif (fuse.startswith("ICPRT")):
               fusedef["icprt"] = collect_fusedef(fp)
            elif (fuse.startswith("IESO")):
               fusedef["ieso"] = collect_fusedef(fp)
            elif (fuse.startswith("IOSCFS")):
               fusedef["ioscfs"] = collect_fusedef(fp)
            elif (fuse.startswith("LVP")):
               fusedef["lvp"] = collect_fusedef(fp)
            elif (fuse.startswith("MCLR")):
               fusedef["mclr"] = collect_fusedef(fp)
            elif (fuse.startswith("OSC:") | (fuse == "OSC")):
               fusedef["osc"] = collect_fusedef(fp)
            elif (fuse.startswith("PLLDIV")):
               fusedef["plldiv"] = collect_fusedef(fp)
            elif (fuse.startswith("PLLEN")):
               fusedef["pllen"] = collect_fusedef(fp)
            elif (fuse.startswith("RSTOSC")):
               fusedef["rstosc"] = collect_fusedef(fp)
            elif (fuse.startswith("USBDIV")):
               fusedef["usbdiv"] = collect_fusedef(fp)
            elif (fuse.startswith("VREGEN")):
               fusedef["vregen"] = collect_fusedef(fp)
            elif (fuse.startswith("WDT:") | (fuse == "WDT")):
               fusedef["wdt"] = collect_fusedef(fp)
            elif (fuse.startswith("XINST")):
               fusedef["xinst"] = collect_fusedef(fp)
            elif (fuse.startswith("JTAGEN")):               # Find JTAGEN since it must be disabled.
               fusedef["jtagen"] = collect_fusedef(fp)
            elif (fuse.startswith("MVECEN")):               # Find Multi Vectored Interrupt since it must be disabled.
               fusedef["mvecen"] = collect_fusedef(fp)
         else:
            if (ln.find(" WDTCON_SWDTEN ") >= 0):
               var["wdtcon_swdten"] = True                           # has field
            elif (ln.find(" USB_BDT_ADDRESS ") >= 0):
               var["usb_bdt"] = True
            elif (ln.find(" OSCCON_IRCF ") >= 0):
               if (ln.find("bit*2") >= 0):
                  var["ircfwidth"] = 2
               elif (ln.find("bit*3") >= 0):
                  var["ircfwidth"] = 3
               elif (ln.find("bit*4") >= 0):
                  var["ircfwidth"] = 4
            elif (ln.find(" OSCCON_SCS ") >= 0):
               var["osccon_scs"] = True
            elif (ln.find(" OSCCON_SPLLEN ") >= 0):
               var["osccon_spllen"] = True
            elif (ln.find(" OSCFRQ_FRQ3 ") >= 0): # For PICs running at 64 MHzm we need to check for bit 4 since ...
               var["oscfrq_frq3"] = True          # ... OSCFRQ_HFFRQ also exists but should not be used.
            elif (ln.find(" OSCFRQ_HFFRQ ") >= 0):
               var["oscfrq_hffrq"] = True
            elif (ln.find(" OSCFRQ_FRQ ") >= 0):
               var["oscfrq_frq"] = True
            # RJ: Fix issue with newer PICs with 4-bit OSCFRQ_HFFRQ3 register
            elif (ln.find(" OSCFRQ_HFFRQ3 ") >= 0):
               var["oscfrq_hffrq3"] = True
            elif (ln.find(" OSCCON1_NOSC ") >= 0):
               var["osccon1_nosc"] = True
            elif (ln.find(" OSCCON1_NDIV ") >= 0):
               var["osccon1_ndiv"] = True
            elif (ln.find(" OSCTUNE_PLLEN ") >= 0):
               var["osctune_pllen"] = True
      ln = fp.readline()
   fp.close()
   return var

# ------------------------------------------------
def find_blinkpin(devfile):
   """ Find suitable pin for LED in range pin_A0..pin_C7
       First choice is pin_A0, but must be checked with device file.
   """
   with open(os.path.join(devdir, devfile), "r") as fp:
      fstr = fp.read()                             # whole file
   ports = ("A", "B", "C")                         # possible ports
   for p in ports:
      for q in range(8):                           # possible pin numbers (0..7)
         pinpq = "pin_%c%d" % (p, q)               # pin name
         if (pinpq in fstr):                       # pin present
            pinpq_dir = pinpq + "_direction"
            if (pinpq_dir in fstr):                # pin direction present
               return pinpq                        # use this pin
            else:                                  # no TRIS-bit found
               print("   Found", pinpq, "but no", pinpq_dir,  "skip this pin.")
   print("   Could not find suitable I/O pin for LED")
   return ""


# -------------------------------------------------
def validate_jalfile(jalfile):
   """ Validate JAL file
       Can be device file or sample program
   """

   cmdlist = [python_exec, "jallib3.py", "validate", jalfile]
   vlog = os.path.join(dstdir, os.path.split(jalfile)[1][:-4] + ".vlog")
   if os.path.exists(vlog):
       os.remove(vlog)
   try:
      log = subprocess.check_output(cmdlist, stderr=subprocess.STDOUT,
                                   universal_newlines=True, shell=False)
   except subprocess.CalledProcessError as e:         #
      with open(vlog, "w") as fp:
         print(e.output, file=fp)                     # save compiler output
      print("   Validation failed for", jalfile)
      print("   See", vlog, "for details")
      return False
#  print "   Validation of", jalfile, "successful!"
   return True


# ----------------------------------------------------
def compile_sample(runtype, pgmname):
   """ Compile sample program and check the result
       Return True if compilation without errors or warnings
       and move sample to destination directory
       Otherwise return False and leave source and compiler output in cwd
   """
   if (runtype == "PROD"):                            # prod mode
      include = ";".join([devprod, incljal])
      smpdir = dstprod                                # destination of created samples
      cmdlist = [compiler, "-no-asm", "-no-codfile", "-no-hex", "-s", include, pgmname]     # compiler options
   else:                                              # test mode
      fhex = os.path.join(dstdir, os.path.splitext(pgmname)[0] + ".hex")     # hex compiler output
      fasm = os.path.join(dstdir, os.path.splitext(pgmname)[0] + ".asm")     # assembler compiler output
   cmdlist = [compiler, "-asm", fasm, "-hex", fhex, "-no-codfile", "-s", devdir, pgmname]     # compiler cmd
   flog = os.path.join(dstdir, pgmname[:-3] + "log")  # compiler output report in test directory
   if (os.path.exists(flog)):
      os.remove(flog)
   destfile = os.path.join(dstdir, pgmname)
   if os.path.exists(destfile):                       # (needed with Windows?)
      os.remove(destfile)

   try:
      log = subprocess.check_output(cmdlist, stderr=subprocess.STDOUT,
                                    universal_newlines=True, shell=False)
      loglist = log.split()                           # make it a list of words
      numerrors = int(loglist[-4])                    # get number of errors
      numwarnings = int(loglist[-2])                  # and warnings
      if ( (numerrors == 0) and (numwarnings == 0) ):
         shutil.move(pgmname, destfile)               # move sample
         if os.path.exists(fhex):                     # remove hex output
            os.remove(fhex)
         if os.path.exists(fasm):                     # remove asm output
            os.remove(fasm)
         return True
      else:
         print("   Compilation of", pgmname, "gave", numerrors, "errors", numwarnings, "warnings")
         shutil.move(pgmname, destfile)            # move sample
         with open(flog, "w") as fp:
            print(log, file=fp)                    # save compiler output
         return False
   except subprocess.CalledProcessError as e:
      shutil.move(pgmname, destfile)               # move sample
      with open(flog, "w") as fp:
         print(e.output, file=fp)                  # save compiler output
      print("   Compilation error(s) with sample", pgmname, "\n   see", flog)
      return False


# -------------------------------------------------
def build_sample(pic, pin, osctype, oscword):
   """ Build blink-a-led sample source file
       Type of oscillator determines contents.
       Returns source file program name if successful, None if not
   """
   pgmname = pic + "_blink"                        # pictype + function
   if (osctype == "HS"):
      pgmname = pgmname + "_hs"                    # OSC ID
   elif (osctype == "INTOSC"):
      pgmname = pgmname + "_intosc"
   elif (osctype == "HS_USB"):
      pgmname = pgmname + "_hs_usb"
   elif (osctype == "INTOSC_USB"):
      pgmname = pgmname + "_intosc_usb"
   else:
      print("   Unrecognized oscillator type:", osctype)
      return None

   picdata = dict(list(devspec[pic.upper()].items()))  # pic specific info

   # No 4 MHz INTOSC for some PICs indicated by mentioning the OSCCON_IRCF in devicespecific.json but
   # without a value ("-").
   # RJ: Maybe this can be removed since ["OSCCON_IRCF"] == "-" is removed from devicespecific.json.
   #     Those devices that where indicated with this option did not have OSCCON_IRCF in the device file.
   if osctype.startswith("INTOSC") & ("OSCCON_IRCF" in picdata):
      if (picdata["OSCCON_IRCF"] == "-"):
         print("   Does not support 4 MHz with internal oscillator")
         return None

   def fusedef_insert(fuse, kwd, cmt):
      """ Insert a fusedef line (if fuse and specific keyword are present)
      """
      if (fuse in fusedef):
         if (kwd in fusedef[fuse]):
            fp.write("pragma target %-8s %-25s " % (fuse.upper(), kwd) + "-- " + cmt + "\n")


   pgmname = pgmname + ".jal"                      # add jal extension
   fp = open(pgmname,  "w")
   fp.write("-- ------------------------------------------------------\n")
   fp.write("-- Title: Blink-a-led of the Microchip pic" + pic + "\n")
   fp.write("--\n")
   yyyy = time.ctime().split()[-1]
   fp.write("-- Author: " + ScriptAuthor + ", Copyright (c) 2008.." + yyyy + " all rights reserved.\n")
   fp.write("--\n")
   fp.write("-- Adapted-by:\n")
   fp.write("--\n")
   fp.write("-- Compiler:" + CompilerVersion + "\n")
   fp.write("--\n")
   fp.write("-- This file is part of jallib (https://github.com/jallib/jallib)\n")
   fp.write("-- Released under the ZLIB license " +
                      "(http://www.opensource.org/licenses/zlib-license.html)\n")
   fp.write("--\n")
   fp.write("-- Description:\n")
   fp.write("--    Simple blink-a-led program for Microchip pic" + pic + "\n")
   if ((osctype == "HS") | (osctype == "HS_USB")):
      fp.write("--    using an external crystal or resonator.\n")
   else:
      fp.write("--    using the internal oscillator.\n")
   fp.write("--    The LED should be flashing twice a second!\n")
   fp.write("--\n")
   fp.write("-- Sources:\n")
   fp.write("--\n")
   fp.write("-- Notes:\n")
   fp.write("--  - Creation date/time: " + datetime.datetime.now().ctime() + "\n")
   fp.write("--  - This file is generated by 'blink-a-led.py' script! Do not change!\n")
   fp.write("--\n")
   fp.write("-- ------------------------------------------------------\n")
   fp.write("--\n")
   fp.write("include "  + pic + "                     -- target PICmicro\n")
   fp.write("--\n")

   # oscillator selection
   if (osctype == "HS"):                                # HS crystal or resonator
      fp.write("-- This program assumes that a 20 MHz resonator or crystal\n")
      fp.write("-- is connected to pins OSC1 and OSC2.\n")
      fp.write("pragma target clock 20_000_000      -- oscillator frequency\n")
      fp.write("--\n")
      fp.write("pragma target OSC      %-25s " % (oscword) + "-- crystal or resonator\n")
      if ("fosc2" in fusedef):
         fp.write("pragma target FOSC2    %-25s " % ("ON") + "-- system clock: OSC\n")
      if ("rstosc" in fusedef):
         if ("EXT1X" in fusedef["rstosc"]):
            fp.write("pragma target RSTOSC   %-25s " % ("EXT1X") + "-- power-up clock select: OSC\n")
      if (oscword == "PRI"):
         fp.write("pragma target POSCMD   %-25s " % ("HS") +  "-- high speed\n")

   elif ((osctype == "INTOSC") | (osctype == "")):    # internal oscillator
      fp.write("-- This program uses the internal oscillator at 4 MHz.\n")
      fp.write("pragma target clock    4_000_000       -- oscillator frequency\n")
      fp.write("--\n")
      # For older versions without OSC, we skip the OSC when it has the value of F4MHZ.
      # F4MHZ is written later (also for other PICs) at ioscfs.
      if (oscword != "F4MHZ"):  # PIC has fuse_def OSC
         fp.write("pragma target OSC      %-25s " % (oscword) + "-- internal oscillator\n")
      fusedef_insert("fosc2", "OFF", "Internal Oscillator")
      fusedef_insert("ioscfs", "F4MHZ", "select 4 MHz")
      if ("oscfrq_frq3" in var):
         fusedef_insert("rstosc", "HFINTOSC_64MHZ", "select 64 MHz")
      elif (("oscfrq" in var) | ("oscfrq_hffrq" in var)):
         fusedef_insert("rstosc", "HFINT32", "select 32 MHz")
      elif ("oscfrq_frq" in var):
         fusedef_insert("rstosc", "HFINTOSC_32MHZ", "select 32 MHz")
   elif (osctype == "HS_USB"):                    # HS oscillator and USB
      fp.write("-- This program assumes that a 20 MHz resonator or crystal\n")
      fp.write("-- is connected to pins OSC1 and OSC2, and USB active.\n")
      fp.write("-- But PIC will be running at 48MHz.\n")
      fp.write("pragma target clock 48_000_000      -- oscillator frequency\n")
      fp.write("--\n")
      fp.write("pragma target OSC      %-25s " % (oscword) + "-- HS osc + PLL\n")
   elif (osctype == "INTOSC_USB"):                   # internal oscillator + USB
      fp.write("-- This program uses the internal oscillator with PLL active.\n")
      fp.write("pragma target clock 48_000_000      -- oscillator frequency\n")
      fp.write("--\n")
      fp.write("pragma target OSC      %-25s " % (oscword) + "-- internal oscillator\n")
      fusedef_insert("fosc2", "OFF", "Internal oscillator")


   # other OSC related fuse_defs
   if ("pllen" in fusedef):                          # PLLEN present
      if (osctype == "INTOSC"):                      # INTOSC selected
         if ("PLLEN" in picdata):
            fusedef_insert("pllen", "ENABLED", "PLL on")
         else:
            fusedef_insert("pllen", "DISABLED", "PLL off")
      elif (osctype == "INTOSC_USB"):
         fusedef_insert("pllen", "ENABLED", "PLL on")
      else:
         fusedef_insert("pllen", "DISABLED", "PLL off")

   if ("plldiv" in fusedef):
      if (osctype == "HS_USB"):
         fusedef_insert("plldiv", "P5", "20 MHz -> 4 MHz")
      elif (osctype == "INTOSC_USB"):
         fusedef_insert("plldiv", "P2", "8 MHz -> 4 MHz")
      else:
         fusedef_insert("plldiv", "P1", "clock postscaler")

   fusedef_insert("cpudiv", "P1", "Fosc divisor")

   if (osctype == "HS_USB"):
      fusedef_insert("usbdiv", "P2", "USB clock selection")

   # now the "easy" fuse_defs!
   fusedef_insert("clkouten", "DISABLED", "no clock output")
   wdtword = ""
   if ("wdt" in fusedef):
      if ("DISABLED" in fusedef["wdt"]):
         fp.write("pragma target WDT      %-25s " % ("DISABLED") + "-- watchdog\n")
         wdtword = "DISABLED"
      elif ("CONTROL", fusedef["wdt"]):
         fp.write("pragma target WDT      %-25s " % ("CONTROL") + "-- watchdog\n")
         wdtword = "CONTROL"
   fusedef_insert("xinst", "DISABLED", "do not use extended instructionset")
   fusedef_insert("debug", "DISABLED", "no debugging")
   fusedef_insert("brownout", "DISABLED", "no brownout reset")
   fusedef_insert("fcmen", "DISABLED", "no clock monitoring")
   fusedef_insert("cswen", "ENABLED", "allow writing OSCCON1 NOSC and NDIV")
   fusedef_insert("ieso", "DISABLED", "no int/ext osc switching")
   fusedef_insert("vregen", "ENABLED", "voltage regulator used")
   fusedef_insert("lvp", "ENABLED", "low voltage programming")
   fusedef_insert("mclr", "EXTERNAL", "external reset")
   fusedef_insert("mvecen", "DISABLED", "Do not use multi vectored interrupts")
   fusedef_insert("jtagen", "DISABLED", "no JTAG to enable all I/O pins")
   fp.write("--\n")
   fp.write("-- The configuration bit settings above are only a selection, sufficient\n")
   fp.write("-- for this program. Other programs may need more or different settings.\n")
   fp.write("--\n")

   if (wdtword == "CONTROL"):
      if ("wdtcon_swdten" in var):
         fp.write("WDTCON_SWDTEN = OFF                 -- disable WDT\n")

   if (osctype == "HS"):                             # HS crystal / resonator
      if ("osccon_scs" in var):
         fp.write("OSCCON_SCS = 0                      -- select primary oscillator\n")
      if ("osctune_pllen" in var):
         fp.write("OSCTUNE_PLLEN = FALSE               -- no PLL\n")
   elif (osctype == "INTOSC"):                       # internal oscillator
      if ("osccon_scs" in var):
         fp.write("OSCCON_SCS = 0                      -- select primary oscillator\n")
      if ("oscfrq_frq3" in var):
         fp.write("OSCFRQ_HFFRQ = 0b0010               -- Fosc 64 -> 4 MHz\n")
      elif ("oscfrq_hffrq3" in var):
         # 4-bit HFFRQ register. For these PICs, check for OSCCON1_NOSC register is required
         # to the the correct frequency. But first check if we can use OSSCON1_NDIV instead.
         if ("osccon1_ndiv" in var):
            fp.write("OSCCON1_NDIV = 0b0011               -- Fosc 32 / 8 -> 4 MHz\n")
         else:
            # Use the combination OSCFRQ_HFFRQ and OSCCON1_NOSC
            fp.write("OSCFRQ_HFFRQ = 0b0011               -- Fosc 32 -> ...\n")
            fp.write("OSCCON1_NOSC = 0b110                -- ... 4 MHz\n")
      elif ("oscfrq_hffrq" in var):
         # 3-bit HFFRQ register.
         fp.write("OSCFRQ_HFFRQ = 0b010                -- Fosc 32 -> 4 MHz\n")
      elif ("oscfrq_frq" in var):
         fp.write("OSCFRQ_FRQ = 0b010                  -- Fosc 32 -> 4 MHz\n")
      if ("ircfwidth" in var):
         if (var["ircfwidth"] > 0) & ("OSCCON_IRCF" in picdata):
            fp.write("OSCCON_IRCF = 0b%-5s" % picdata["OSCCON_IRCF"] + "               -- 4 MHz\n")
      if ("osctune_pllen" in var):
         fp.write("OSCTUNE_PLLEN = FALSE               -- no PLL\n")
      if ("osccon_spllen" in var):
         fp.write("OSCCON_SPLLEN = FALSE               -- software PLL off\n")
   elif (osctype == "HS_USB"):                       # HS cryst./res. + USB
      if ("osccon_scs" in var):
         fp.write("OSCCON_SCS = 0                      -- select primary oscillator\n")
      if ("osctune_pllen" in var):
         fp.write("OSCTUNE_PLLEN = TRUE                -- PLL\n")
   elif (osctype == "INTOSC_USB"):                   # internal oscillator + USB
      if ("osccon_scs" in var):
         fp.write("OSCCON_SCS = 0                      -- select primary oscillator\n")
      if ("osctune_pllen" in var):
         fp.write("OSCTUNE_PLLEN = TRUE                -- use PLL\n")

   # the actual blink-a-led program code
   fp.write("--\n")
   fp.write("enable_digital_io()                 -- make all pins digital I/O\n")
   fp.write("--\n")
   fp.write("-- A low current (2 mA) led with 2.2K series resistor is recommended\n")
   fp.write("-- since the chosen pin may not be able to drive an ordinary 20mA led.\n")
   fp.write("--\n")
   fp.write("alias  led       is " + pin + "          -- alias for pin with LED\n")
   fp.write("--\n")
   fp.write(pin + "_direction = OUTPUT\n")
   fp.write("--\n")
   fp.write("forever loop\n")
   fp.write("   led = ON\n")
   fp.write("   _usec_delay(100_000)\n")
   fp.write("   led = OFF\n")
   fp.write("   _usec_delay(400_000)\n")
   fp.write("end loop\n")
   fp.write("--\n")
   fp.close()                                         # blink sample complete!
   return pgmname


# -----------------------------------------------------
def build_validate_compile_sample(pic, blink_pin, osctype, oscword):
   """ Build, validate and compile a sample
       Chack result of compile for no errors and warnings
   """
   pgmname = build_sample(pic, blink_pin, osctype, oscword)
   if (pgmname == None):
      print("   No sample for", pic)
      return False
   print(pgmname)
   if (not validate_jalfile(pgmname)):
      return False                                    # validate failed
   if (not compile_sample(runtype, pgmname)):
      return False
   return True                                        # Everythng OK


# ----------------------------------------------------
def main(runtype, devs):
   """ Create one or more blink-a-led samples for every device file
       Arguments: runtype: PROD or TEST
                  devs: list of device files for which to build a blink sample
   """
   sample_count = 0

   def create_sample():
      counter = 0
      picname = os.path.splitext(dev)[0]
      # We generate samples for all possible types, HS, INTOSC, USB
      if (osctype == "HS"):  # this was a HS type
         if (build_validate_compile_sample(picname, blink_pin, osctype, oscword)):  # primary sample OK
            counter += 1
      elif (("ioscfs" in fusedef) & ("osc" not in fusedef)): # Older PICs
         if ("F4MHZ" in fusedef["ioscfs"]):
            if (build_validate_compile_sample(picname, blink_pin, "INTOSC", "F4MHZ")):
               counter += 1
      elif ("osc" in fusedef):
         # Build as most 2 internal oscillator variants, one without USB and one with (if present)
         if ("INTOSC_NOCLKOUT" in fusedef["osc"]):  # no intosc + pll
            if (build_validate_compile_sample(picname, blink_pin, "INTOSC", "INTOSC_NOCLKOUT")):
               counter += 1
         elif ("INTOSC_NOCLKOUT_USB_HS" in fusedef["osc"]):  # intosc + pll
            if (build_validate_compile_sample(picname, blink_pin, "INTOSC", "INTOSC_NOCLKOUT_USB_HS")):
               counter += 1
         elif ("INTOSC_NOCLKOUT_PLL" in fusedef["osc"]):
            if (build_validate_compile_sample(picname, blink_pin, "INTOSC_USB", "INTOSC_NOCLKOUT_PLL")):
               counter += 1
         elif ("OFF" in fusedef["osc"]):
            if (build_validate_compile_sample(picname, blink_pin, "INTOSC", "OFF")):
               counter += 1
         elif ("fosc2" in fusedef):
            if ("ON" in fusedef["fosc2"]): # "implicit" fuse_def intosc
               if ("EC_CLKOUT_PLL" in fusedef["osc"]):
                  if (build_validate_compile_sample(picname, blink_pin, "INTOSC", "EC_CLKOUT_PLL")):
                     counter += 1
               elif ("INTOSC_NOCLKOUT_PLL" in fusedef["osc"]):
                  if (build_validate_compile_sample(picname, blink_pin, "INTOSC", "INTOSC_NOCLKOUT")):
                     counter += 1
         # The USB variant.
         if (("HS_PLL" in fusedef["osc"]) & ("usb_bdt" in var)):
            if (build_validate_compile_sample(picname, blink_pin, "HS_USB", "HS_PLL")):
               counter += 1
      return counter

   for dev in devs:
      if (runtype == "PROD"):                         # production device file
         jalfile = os.path.join(devprod, dev)
      else:                                           # test device file
         jalfile = os.path.join(devdir, dev)
      if (not validate_jalfile(jalfile)):             # device file does not validate
         continue

      var = scan_devfile(dev)                         # build list of selected device info
                                                      # builds also fusedef
      blink_pin = find_blinkpin(dev)
      if (blink_pin == ""):                           # no blink pin available
         continue

      current_sample_count = sample_count
      if ("osc" not in fusedef):                      # no fusedef osc at all
         osctype = "INTOSC"                           # must be internal oscillator
         if (("ioscfs" in fusedef) & ("f4mhz" in var)):
            oscword = "f4mhz"
         else:
            oscword = "" # without fuse_def OSC
         sample_count = sample_count + create_sample()
      else:
         if ("OFF" in fusedef["osc"]):                 # 16f19155, etc. Check moved upward to have internal oscillator ...
            osctype = "INTOSC"                           # .. as preference before HS.
            oscword = "OFF"
            sample_count = sample_count + create_sample()
         if ("INTOSC_NOCLKOUT" in fusedef["osc"]):     # First look for internal oscillator.
            osctype = "INTOSC"
            oscword = "INTOSC_NOCLKOUT"
            sample_count = sample_count + create_sample()
         if ("HSH" in fusedef["osc"]):
            osctype = "HS"
            oscword = "HSH"
            sample_count = sample_count + create_sample()
         if ("PRI" in fusedef["osc"]):
            osctype = "HS"
            oscword = "PRI"
            sample_count = sample_count + create_sample()
         if ("HS" in fusedef["osc"]):
            osctype = "HS"
            oscword = "HS"
            sample_count = sample_count + create_sample()
      if (current_sample_count == sample_count):
         print("   Could not detect a suitable OSC keyword in for", dev)
         continue                                     # skip this PIC

   return sample_count





# ======== E N T R Y   P O I N T  =======================================

if (__name__ == "__main__"):
   """ Process commandline arguments, start process, clock execution time
   """
   if (len(sys.argv) > 1):
      runtype = sys.argv[1].upper()
   else:
      print("Specify at least PROD or TEST as first argument")
      print("and optionally as second argument a pictype (wildcards allowed)")
      sys.exit(1)

   if (len(sys.argv) > 3):
      print("Expecting not more than 2 arguments: runtype + selection")
      print("==> When using wildcards, specify selection string between quotes")
      print("    or use the command 'set -f' to suppress wildcard expansion by the shell")
      sys.exit(1)
   elif (len(sys.argv) > 2):
      selection = sys.argv[2] + ".jal"                # add extension
   else:
      selection = "1*.jal"                            # default selection

   print("Creating blink-a-led sample files")
   read_devspec_file()  # PIC specific info, like OSCCON_IRCF #
   elapsed = time.time()
   cwd = os.getcwd()                                  # remember working directory
   if (runtype == "PROD"):
      print("PROD option temporary disabled")
      sys.exit(1)
   elif (runtype == "TEST"):
      if (not os.path.exists(os.path.join(devdir, "chipdef_jallib.jal"))):
         print("Probably no device files in", devdir)
         sys.exit(1)
   os.chdir(devdir)                                   # dir with device files
   devs = glob.glob(selection)                        # list of device files
   os.chdir(cwd)                                      # back to working dir
   if (len(devs) == 0):
      print("No device files found matching", selection)
      sys.exit(1)
   devs.sort()                                        # alphanumeric order

   count = main(runtype, devs)                        # the actual process

   elapsed = time.time() - elapsed
   if (elapsed > 0):
      print("Generated %d blink-a-led samples in %.1f seconds (%.1f per second)" % \
             (count, elapsed, count / elapsed))


