#! /usr/bin/perl

#ー―ー―ー―ー―ー―ー―ー―ー―ー―ー―ー
#― 	-      BR MAIN SCRIPT      - 	 ―
#ー 									 ー
#― 	�@�@	�l�{�任@蹄	�@�@		 ―
#ー 									 ー
#― MAIN	-	�D�n�B�z				 ―
#ー COM		-	���O�B�z�@�@			 ー
#― HEAL	-	�v潜�B�z				 ―
#ー INN		-	採�v�B�z				 ー
#― INNHEAL	-	�R�i�B�z				 ―
#ー BB_CK	-	ぃタ訣�s蹄┥ゎ�@�@�@	 ー
#―ー―ー―ー―ー―ー―ー―ー―ー―ー―ー―

#require"jcode.pl";
require"br.cgi";
require"$LIB_DIR/lib1.cgi";

&LOCK;
require"pref.cgi";
&DECODE;
&CREAD;
&IDCHK;
if ($mode eq "main"){&MAIN;}
elsif ($mode eq "command"){&COM;}
else {&ERROR("ぃタ訣�些X維","No Command selected","BATTLE");}
&UNLOCK;
exit;
#==================#
# ― �D�n�B�z	   #
#==================#
sub MAIN {
	&HEADER;
	require"$LIB_DIR/disp_sts.cgi";
	require"$LIB_DIR/disp_cmd.cgi";
	&STS();
	&FOOTER;
}
#==================#
# ― ���O�B�z�@�@  #
#==================#
sub COM {
#々 仮以�P惜�繊P較�Q��
if (($Command eq "MOVE")&&($Command2 =~ /MV/))	{require "$LIB_DIR/lib2.cgi";&MOVE;}				#仮以
elsif($Command eq "SEARCH")						{require "$LIB_DIR/lib2.cgi";&SEARCH;}				#唄��
elsif($Command =~ /GET_/)						{require "$LIB_DIR/lib2.cgi";&WINGET;}				#菖�Q�~
#々 �豐_�B�z魁
elsif($Command eq "kaifuku"){	if($Command5 eq "HEAL")		{&HEAL;}								#�v潜
								if($Command5 eq "INN")		{&INN;}									#採�v
								if($Command5 eq "INNHEAL")	{&INNHEAL;}}							#�R�i
elsif($Command eq "HEAL")	{&HEAL;}																#�v潜
elsif($Command eq "INN")	{&INN;}																	#採�v
elsif($Command eq "INNHEAL"){&INNHEAL;}																#�R�i
#々 ITEM1
elsif($Command =~ /ITEM_/)			{require "$LIB_DIR/item1.cgi";&ITEM;}							#�D�礙魯�
elsif($Command =~ /DEL_/)			{require "$LIB_DIR/item1.cgi";&ITEMDEL;}						#�D�祓鷂m
elsif($Command eq "ITEMDELNEW")		{require "$LIB_DIR/item1.cgi";&ITEMDELNEW;}						#�D�礇甕�
elsif($Command eq "ITEMGETNEW")		{require "$LIB_DIR/item1.cgi";&ITEMGETNEW;}						#�D�秕潭B
elsif($Command =~ /ITEMNEWXCG_/)	{require "$LIB_DIR/item1.cgi";&ITEMNEWXCG;}						#�D�礇羇�
elsif($Command eq "ITMAIN"){if($Command3 eq "WEPDEL")	{require "$LIB_DIR/item1.cgi";&WEPDEL;}		#�Z捷娃�U
							if($Command3 eq "WEPDEL2")	{require "$LIB_DIR/item1.cgi";&WEPDEL2;}	#�Z捷メ遠
							if($Command3 eq "BOUDELH")	{require "$LIB_DIR/item1.cgi";&BOUDELH;}	#�Y┥�祕��U
							if($Command3 eq "BOUDELB")	{require "$LIB_DIR/item1.cgi";&BOUDELB;}	#悼┥�祕��U
							if($Command3 eq "BOUDELA")	{require "$LIB_DIR/item1.cgi";&BOUDELA;}	#誼┥�祕��U
							if($Command3 eq "BOUDELF")	{require "$LIB_DIR/item1.cgi";&BOUDELF;}	#━┥�祕��U
							if($Command3 eq "BOUDEL")	{require "$LIB_DIR/item1.cgi";&BOUDEL;}}	#庫喉�~娃�U
#々 ATTACK
elsif($Command =~ /ATK/)		{require "$LIB_DIR/attack.cgi";require"$LIB_DIR/lib4.cgi";&ATTACK1;}#ю聖
elsif($Command eq "RUNAWAY")	{require "$LIB_DIR/attack.cgi";&RUNAWAY;}							#�k�`
#々 LIB3
elsif($Command =~ /OUK_/)								{require"$LIB_DIR/lib3.cgi";&OUKYU;}		#棲�羈B�m
elsif(($msg2 ne "")||($dmes2 ne "")||($com2 ne ""))		{require"$LIB_DIR/lib3.cgi";&WINCHG;}		#�f�Y�y怒��
elsif(($teamID2 ne "")||($teamPass2 ne ""))				{require"$LIB_DIR/lib3.cgi";&TEAM;}			#�p箇賞�@
elsif($Command eq "SPECIAL"){if($Command4 eq "SPEAKER")	{require "$LIB_DIR/lib3.cgi";&SPEAKER;}		#亭�a喚�n捷�魯�
							 if($Command4 eq "HACK")	{require "$LIB_DIR/lib3.cgi";&HACKING;}}	#Hacking
elsif($Command =~ /KOU_/)		{require"$LIB_DIR/lib3.cgi";&KOUDOU;}								#芋セよ�w
elsif($Command =~ /OUS_/)		{require"$LIB_DIR/lib3.cgi";&OUSEN;}								#棲菖よ�w
elsif ($Command eq "SEVE")		{require"$LIB_DIR/lib3.cgi";&SEVE;}									#Messener
elsif($Command =~ /POI_/)		{require "$LIB_DIR/lib3.cgi";&POISON;}								#�r���V�J
elsif($Command =~ /PSC_/)		{require "$LIB_DIR/lib3.cgi";&PSCHECK;}								#�r┌
#々 ITEM2
elsif(($Command =~ /SEIRI_/)&&($Command2 =~ /SEIRI2_/)){require "$LIB_DIR/item2.cgi";&ITEMSEIRI;}	#�D�秕祺z
elsif(($Command =~ /GOUSEI1_/)&&($Command2 =~ /GOUSEI2_/)&&($Command3 =~ /GOUSEI3_/))
														{require "$LIB_DIR/item2.cgi";&ITEMGOUSEI;}	#�D�礒XΘ
elsif(($Command =~ /SEITO_/)&&($Command2 =~ /JO_/)) {require "$LIB_DIR/item2.cgi";&ITEMJOUTO;}		#�D�秣狹�
#々 ADMIN
elsif($Command eq "BSAVE")	{require "admin.cgi";&BACKSAVE;}										#�O�s
elsif($Command eq "BREAD")	{require "admin.cgi";&BACKREAD;}										#的�J
elsif($Command eq "RESET")	{require "admin.cgi";&DATARESET;}										#�讒lて
#々 �蹈楹�
if(($Command =~ /BATTLE/)||($Command =~ /ATK/))
		{&HEADER;require "$LIB_DIR/disp_att.cgi";require"$LIB_DIR/disp_cmd.cgi";&BATTLE;&FOOTER;}	#菖茜飢�G
elsif($Command eq "ITEMJOUTO")
		{&HEADER;require "$LIB_DIR/disp_att.cgi";require"$LIB_DIR/disp_cmd.cgi";&BATTLE;&FOOTER;}	#�D�秣狹�
elsif ($mflg ne "ON") {&MAIN;}
}
#===========================#
# ― �v潜�P採�v�P�R�i�B�z�@	#
#===========================#
sub HEAL	{$sts = "�v潜";$endtime = $now;&SAVE;}
sub INN		{$sts = "採�v";$endtime = $now;&SAVE;}
sub INNHEAL	{$sts = "�R�i";$endtime = $now;&SAVE;}
#===========================#
# ― ぃタ訣�s蹄┥ゎ�@�@�@�@ #
#===========================#
sub BB_CK{if($wf eq $w_id){$wf = "";}else{&ERROR("ぃタ訣�X維�C","Used Browser Back Command","BATTLE-BB_CK");}}
1;
