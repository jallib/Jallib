/** \file
 *  This C header file was generated by $ANTLR version 3.2 Sep 23, 2009 12:02:23
 *
 *     -  From the grammar source file : jal.g
 *     -                            On : 2010-04-13 08:38:19
 *     -                 for the lexer : jalLexerLexer *
 * Editing it, at least manually, is not wise. 
 *
 * C language generator and runtime by Jim Idle, jimi|hereisanat|idle|dotgoeshere|ws.
 *
 *
 * The lexer jalLexer has the callable functions (rules) shown below,
 * which will invoke the code for the associated rule in the source grammar
 * assuming that the input stream is pointing to a token/text stream that could begin
 * this rule.
 * 
 * For instance if you call the first (topmost) rule in a parser grammar, you will
 * get the results of a full parse, but calling a rule half way through the grammar will
 * allow you to pass part of a full token stream to the parser, such as for syntax checking
 * in editors and so on.
 *
 * The parser entry points are called indirectly (by function pointer to function) via
 * a parser context typedef pjalLexer, which is returned from a call to jalLexerNew().
 *
 * As this is a generated lexer, it is unlikely you will call it 'manually'. However
 * the methods are provided anyway.
 * * The methods in pjalLexer are  as follows:
 *
 *  -  void      pjalLexer->T__17(pjalLexer)
 *  -  void      pjalLexer->T__18(pjalLexer)
 *  -  void      pjalLexer->T__19(pjalLexer)
 *  -  void      pjalLexer->T__20(pjalLexer)
 *  -  void      pjalLexer->T__21(pjalLexer)
 *  -  void      pjalLexer->T__22(pjalLexer)
 *  -  void      pjalLexer->T__23(pjalLexer)
 *  -  void      pjalLexer->T__24(pjalLexer)
 *  -  void      pjalLexer->T__25(pjalLexer)
 *  -  void      pjalLexer->T__26(pjalLexer)
 *  -  void      pjalLexer->T__27(pjalLexer)
 *  -  void      pjalLexer->T__28(pjalLexer)
 *  -  void      pjalLexer->T__29(pjalLexer)
 *  -  void      pjalLexer->T__30(pjalLexer)
 *  -  void      pjalLexer->T__31(pjalLexer)
 *  -  void      pjalLexer->T__32(pjalLexer)
 *  -  void      pjalLexer->T__33(pjalLexer)
 *  -  void      pjalLexer->T__34(pjalLexer)
 *  -  void      pjalLexer->T__35(pjalLexer)
 *  -  void      pjalLexer->T__36(pjalLexer)
 *  -  void      pjalLexer->T__37(pjalLexer)
 *  -  void      pjalLexer->T__38(pjalLexer)
 *  -  void      pjalLexer->T__39(pjalLexer)
 *  -  void      pjalLexer->T__40(pjalLexer)
 *  -  void      pjalLexer->T__41(pjalLexer)
 *  -  void      pjalLexer->T__42(pjalLexer)
 *  -  void      pjalLexer->T__43(pjalLexer)
 *  -  void      pjalLexer->T__44(pjalLexer)
 *  -  void      pjalLexer->T__45(pjalLexer)
 *  -  void      pjalLexer->T__46(pjalLexer)
 *  -  void      pjalLexer->T__47(pjalLexer)
 *  -  void      pjalLexer->T__48(pjalLexer)
 *  -  void      pjalLexer->T__49(pjalLexer)
 *  -  void      pjalLexer->T__50(pjalLexer)
 *  -  void      pjalLexer->T__51(pjalLexer)
 *  -  void      pjalLexer->T__52(pjalLexer)
 *  -  void      pjalLexer->T__53(pjalLexer)
 *  -  void      pjalLexer->T__54(pjalLexer)
 *  -  void      pjalLexer->T__55(pjalLexer)
 *  -  void      pjalLexer->T__56(pjalLexer)
 *  -  void      pjalLexer->T__57(pjalLexer)
 *  -  void      pjalLexer->T__58(pjalLexer)
 *  -  void      pjalLexer->T__59(pjalLexer)
 *  -  void      pjalLexer->T__60(pjalLexer)
 *  -  void      pjalLexer->T__61(pjalLexer)
 *  -  void      pjalLexer->T__62(pjalLexer)
 *  -  void      pjalLexer->T__63(pjalLexer)
 *  -  void      pjalLexer->T__64(pjalLexer)
 *  -  void      pjalLexer->T__65(pjalLexer)
 *  -  void      pjalLexer->T__66(pjalLexer)
 *  -  void      pjalLexer->T__67(pjalLexer)
 *  -  void      pjalLexer->T__68(pjalLexer)
 *  -  void      pjalLexer->T__69(pjalLexer)
 *  -  void      pjalLexer->T__70(pjalLexer)
 *  -  void      pjalLexer->T__71(pjalLexer)
 *  -  void      pjalLexer->T__72(pjalLexer)
 *  -  void      pjalLexer->T__73(pjalLexer)
 *  -  void      pjalLexer->T__74(pjalLexer)
 *  -  void      pjalLexer->T__75(pjalLexer)
 *  -  void      pjalLexer->T__76(pjalLexer)
 *  -  void      pjalLexer->T__77(pjalLexer)
 *  -  void      pjalLexer->T__78(pjalLexer)
 *  -  void      pjalLexer->T__79(pjalLexer)
 *  -  void      pjalLexer->T__80(pjalLexer)
 *  -  void      pjalLexer->T__81(pjalLexer)
 *  -  void      pjalLexer->T__82(pjalLexer)
 *  -  void      pjalLexer->T__83(pjalLexer)
 *  -  void      pjalLexer->T__84(pjalLexer)
 *  -  void      pjalLexer->T__85(pjalLexer)
 *  -  void      pjalLexer->T__86(pjalLexer)
 *  -  void      pjalLexer->T__87(pjalLexer)
 *  -  void      pjalLexer->T__88(pjalLexer)
 *  -  void      pjalLexer->T__89(pjalLexer)
 *  -  void      pjalLexer->T__90(pjalLexer)
 *  -  void      pjalLexer->T__91(pjalLexer)
 *  -  void      pjalLexer->IDENTIFIER(pjalLexer)
 *  -  void      pjalLexer->LETTER(pjalLexer)
 *  -  void      pjalLexer->BIN_LITERAL(pjalLexer)
 *  -  void      pjalLexer->DECIMAL_LITERAL(pjalLexer)
 *  -  void      pjalLexer->HEX_LITERAL(pjalLexer)
 *  -  void      pjalLexer->OCTAL_LITERAL(pjalLexer)
 *  -  void      pjalLexer->CHARACTER_LITERAL(pjalLexer)
 *  -  void      pjalLexer->STRING_LITERAL(pjalLexer)
 *  -  void      pjalLexer->HexDigit(pjalLexer)
 *  -  void      pjalLexer->EscapeSequence(pjalLexer)
 *  -  void      pjalLexer->OctalEscape(pjalLexer)
 *  -  void      pjalLexer->WS(pjalLexer)
 *  -  void      pjalLexer->LINE_COMMENT(pjalLexer)
 *  -  void      pjalLexer->Tokens(pjalLexer)
 *
 * The return type for any particular rule is of course determined by the source
 * grammar file.
 */
// [The "BSD licence"]
// Copyright (c) 2005-2009 Jim Idle, Temporal Wave LLC
// http://www.temporal-wave.com
// http://www.linkedin.com/in/jimidle
//
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions
// are met:
// 1. Redistributions of source code must retain the above copyright
//    notice, this list of conditions and the following disclaimer.
// 2. Redistributions in binary form must reproduce the above copyright
//    notice, this list of conditions and the following disclaimer in the
//    documentation and/or other materials provided with the distribution.
// 3. The name of the author may not be used to endorse or promote products
//    derived from this software without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
// IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
// OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
// IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
// INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
// NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
// THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#ifndef	_jalLexer_H
#define _jalLexer_H
/* =============================================================================
 * Standard antlr3 C runtime definitions
 */
#include    <antlr3.h>

/* End of standard antlr 3 runtime definitions
 * =============================================================================
 */
 
#ifdef __cplusplus
extern "C" {
#endif

// Forward declare the context typedef so that we can use it before it is
// properly defined. Delegators and delegates (from import statements) are
// interdependent and their context structures contain pointers to each other
// C only allows such things to be declared if you pre-declare the typedef.
//
typedef struct jalLexer_Ctx_struct jalLexer, * pjalLexer;



#ifdef	ANTLR3_WINDOWS
// Disable: Unreferenced parameter,							- Rules with parameters that are not used
//          constant conditional,							- ANTLR realizes that a prediction is always true (synpred usually)
//          initialized but unused variable					- tree rewrite variables declared but not needed
//          Unreferenced local variable						- lexer rule declares but does not always use _type
//          potentially unitialized variable used			- retval always returned from a rule 
//			unreferenced local function has been removed	- susually getTokenNames or freeScope, they can go without warnigns
//
// These are only really displayed at warning level /W4 but that is the code ideal I am aiming at
// and the codegen must generate some of these warnings by necessity, apart from 4100, which is
// usually generated when a parser rule is given a parameter that it does not use. Mostly though
// this is a matter of orthogonality hence I disable that one.
//
#pragma warning( disable : 4100 )
#pragma warning( disable : 4101 )
#pragma warning( disable : 4127 )
#pragma warning( disable : 4189 )
#pragma warning( disable : 4505 )
#pragma warning( disable : 4701 )
#endif

/** Context tracking structure for jalLexer
 */
struct jalLexer_Ctx_struct
{
    /** Built in ANTLR3 context tracker contains all the generic elements
     *  required for context tracking.
     */
    pANTLR3_LEXER    pLexer;


     void (*mT__17)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__18)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__19)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__20)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__21)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__22)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__23)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__24)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__25)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__26)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__27)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__28)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__29)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__30)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__31)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__32)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__33)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__34)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__35)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__36)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__37)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__38)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__39)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__40)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__41)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__42)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__43)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__44)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__45)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__46)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__47)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__48)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__49)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__50)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__51)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__52)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__53)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__54)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__55)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__56)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__57)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__58)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__59)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__60)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__61)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__62)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__63)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__64)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__65)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__66)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__67)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__68)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__69)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__70)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__71)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__72)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__73)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__74)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__75)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__76)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__77)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__78)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__79)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__80)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__81)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__82)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__83)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__84)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__85)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__86)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__87)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__88)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__89)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__90)	(struct jalLexer_Ctx_struct * ctx);
     void (*mT__91)	(struct jalLexer_Ctx_struct * ctx);
     void (*mIDENTIFIER)	(struct jalLexer_Ctx_struct * ctx);
     void (*mLETTER)	(struct jalLexer_Ctx_struct * ctx);
     void (*mBIN_LITERAL)	(struct jalLexer_Ctx_struct * ctx);
     void (*mDECIMAL_LITERAL)	(struct jalLexer_Ctx_struct * ctx);
     void (*mHEX_LITERAL)	(struct jalLexer_Ctx_struct * ctx);
     void (*mOCTAL_LITERAL)	(struct jalLexer_Ctx_struct * ctx);
     void (*mCHARACTER_LITERAL)	(struct jalLexer_Ctx_struct * ctx);
     void (*mSTRING_LITERAL)	(struct jalLexer_Ctx_struct * ctx);
     void (*mHexDigit)	(struct jalLexer_Ctx_struct * ctx);
     void (*mEscapeSequence)	(struct jalLexer_Ctx_struct * ctx);
     void (*mOctalEscape)	(struct jalLexer_Ctx_struct * ctx);
     void (*mWS)	(struct jalLexer_Ctx_struct * ctx);
     void (*mLINE_COMMENT)	(struct jalLexer_Ctx_struct * ctx);
     void (*mTokens)	(struct jalLexer_Ctx_struct * ctx);    const char * (*getGrammarFileName)();
    void	    (*free)   (struct jalLexer_Ctx_struct * ctx);
        
};

// Function protoypes for the constructor functions that external translation units
// such as delegators and delegates may wish to call.
//
ANTLR3_API pjalLexer jalLexerNew         (pANTLR3_INPUT_STREAM instream);
ANTLR3_API pjalLexer jalLexerNewSSD      (pANTLR3_INPUT_STREAM instream, pANTLR3_RECOGNIZER_SHARED_STATE state);

/** Symbolic definitions of all the tokens that the lexer will work with.
 * \{
 *
 * Antlr will define EOF, but we can't use that as it it is too common in
 * in C header files and that would be confusing. There is no way to filter this out at the moment
 * so we just undef it here for now. That isn't the value we get back from C recognizers
 * anyway. We are looking for ANTLR3_TOKEN_EOF.
 */
#ifdef	EOF
#undef	EOF
#endif
#ifdef	Tokens
#undef	Tokens
#endif 
#define T__29      29
#define T__28      28
#define T__27      27
#define T__26      26
#define T__25      25
#define T__24      24
#define T__23      23
#define LETTER      7
#define T__22      22
#define T__21      21
#define T__20      20
#define EOF      -1
#define T__19      19
#define T__91      91
#define STRING_LITERAL      5
#define T__90      90
#define T__18      18
#define T__17      17
#define BIN_LITERAL      8
#define T__80      80
#define T__81      81
#define T__82      82
#define T__83      83
#define LINE_COMMENT      16
#define CHARACTER_LITERAL      6
#define T__85      85
#define T__84      84
#define T__87      87
#define T__86      86
#define T__89      89
#define T__88      88
#define WS      15
#define T__71      71
#define T__72      72
#define T__70      70
#define T__76      76
#define T__75      75
#define T__74      74
#define EscapeSequence      13
#define DECIMAL_LITERAL      11
#define T__73      73
#define T__79      79
#define T__78      78
#define T__77      77
#define T__68      68
#define T__69      69
#define T__66      66
#define T__67      67
#define T__64      64
#define T__65      65
#define T__62      62
#define T__63      63
#define T__61      61
#define T__60      60
#define HexDigit      12
#define T__55      55
#define T__56      56
#define T__57      57
#define T__58      58
#define T__51      51
#define T__52      52
#define T__53      53
#define T__54      54
#define IDENTIFIER      4
#define T__59      59
#define HEX_LITERAL      9
#define T__50      50
#define T__42      42
#define T__43      43
#define T__40      40
#define T__41      41
#define T__46      46
#define T__47      47
#define T__44      44
#define T__45      45
#define T__48      48
#define T__49      49
#define OCTAL_LITERAL      10
#define T__30      30
#define T__31      31
#define T__32      32
#define T__33      33
#define T__34      34
#define T__35      35
#define T__36      36
#define T__37      37
#define T__38      38
#define T__39      39
#define OctalEscape      14
#ifdef	EOF
#undef	EOF
#define	EOF	ANTLR3_TOKEN_EOF
#endif

#ifndef TOKENSOURCE
#define TOKENSOURCE(lxr) lxr->pLexer->rec->state->tokSource
#endif

/* End of token definitions for jalLexer
 * =============================================================================
 */
/** \} */

#ifdef __cplusplus
}
#endif

#endif

/* END - Note:Keep extra line feed to satisfy UNIX systems */
