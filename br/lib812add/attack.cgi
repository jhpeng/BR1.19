#ー―ー―ー―ー―ー―ー―ー―ー―ー―ー―ー
#― 	-    BR ATTACK PROGRAM    - 	 ―
#ー 									 ー
#― 		�@�@�l�{�任@蹄�@			 ―
#ー 									 ー
#― ATTJYO		-	退統�B�z			 ―
#ー ATTACK		-	���逾霎鯖蹈�		 ー
#― ATTACK1		-	���逾霎山B�z		 ―
#ー ATTACK2		-	�瓰隘霎山B�z		 ー
#― WEPTREAT	-	�Z捷ю聖�B�z		 ―
#ー DEATH		-	�曚畝困`�B�z		 ―
#― DEATH2		-	篠�困`�B�z			 ー
#ー RUNAWAY		-	�k�`�B�z			 ―
#― DEFTREAT	-	┥�禳悋O�B�z		 ー
#ー LVUPCHK		-	汽�迭B�z�@�@�@�@	 ―
#― lvuprand	- �@汽�点H穣�爐O�I�B�z�@ ー
#ー EN_KAIFUKU	-	篠�^�_�B�z			 ―
#― BLOG_CK		-   篠菖茜�朧鮒d娃�B�z �@ー
#ー―ー―ー―ー―ー―ー―ー―ー―ー―ー―ー
#==================#
# ― 退統�B�z	   #
#==================#
sub ATTJYO {
if (($teamID ne "�L")&&($teamID ne "")&&($teamID eq $w_teamID)&&($teamPass eq $w_teamPass)){
	$log = ($log . "$w_f_name $w_l_name ($w_cl $w_sex$w_no�f) �o�{�I<br>") ;
	$log = ($log . "$w_f_name $w_l_name �SΤヴ�鶺o�{...�C<br>") ;
	$Command="ITEMJOUTO";
}else{&ERROR("ぃタ訣�X維","teamID and teamPass missmatch","ATTACK-ATTJYO");}
}
#==================#
# ― ���逾霎鯖蹈�  #
#==================#
sub ATTACK {
$log = ($log . "$w_f_name $w_l_name ($w_cl $w_sex$w_no�f) �o�{�I<br>") ;
$log = ($log . "$w_f_name $w_l_name �o嫡�SΤヴ�鶺o�{...�C<br>") ;
$Command=("BATTLE0" . "_" . $w_id);
}
#==================#
# ― ���逾霎山B�z  #
#==================#
sub ATTACK1 {
require "$LIB_DIR/lib2.cgi";
$kega2 = "" ; $kega3 = "" ;
$hakaiinf2 = ""; $hakaiinf3 = "";

local($i) = 0 ;
local($result) = 0 ;
local($result2) = 0 ;
local($dice1) = int(rand(100)) ;
local($dice2) = int(rand(100)) ;

local($a,$w_kind,$wid) = split(/_/, $Command);

open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
for ($i=0; $i<$#userlist+1; $i++) {
	($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_ousen,$w_seikaku,$w_sinri,$w_item_get,$w_eff_get,$w_itai_get,$w_teamID,$w_teamPass,$w_IP,) = split(/,/, $userlist[$i]);
	if ($w_id eq $wid) {$Index2=$i; last;}
}
#�s茜--->
if ((($tactics ne "�s茜�羂�")&&($w_bid eq $id))||($w_hit <= 0)) {&ERROR("ぃタ訣�X維","rento is not valid","Attack-ATTACK1") ;}
#<---�s茜
&BB_CK; #�s蹄捷�I魁棲刻
$log = ($log . "$w_f_name $w_l_name ($w_cl $w_sex$w_no�f) 菖茜�}�l�I<br>") ;

($w_name,$a) = split(/<>/, $wep);
($w_name2,$w_kind2) = split(/<>/, $w_wep);
&TACTGET; &TACTGET2;	#芋セ�羂�

#悉�饐�
if ((($wep =~ /G|A/) && ($wtai == 0)) || (($wep =~ /G|A/) && ($w_kind eq "WB"))) {$att_p = (($watt/10) + $att) * $atp ;}
else {$att_p = ($watt + $att) * $atp ;}
local($ball) = $def + $bdef + $bdef_h + $bdef_a + $bdef_f ;
if ($item[5] =~ /AD/) {$ball += $eff[5];} #庫喉┥�@�磧H
$def_p = $ball * $dfp ;

#篠
if (($w_wep =~ /G|A/) && ($w_wtai == 0)) {$att_n = (($w_watt/10) + $w_att) * $atn ;}
else {$att_n = ($w_watt + $w_att) * $atn ;}
local($ball2) = $w_def + $w_bdef + $w_bdef_h + $w_bdef_a + $w_bdef_f ;
if ($w_item[5] =~ /AD/) {$ball2 += $w_eff[5];} #庫喉┥�@�磧H
$def_n = $ball2 * $dfn ;

&BLOG_CK;
&EN_KAIFUKU;

$Command="BATTLE";

if ($w_pls ne $pls) {$log = ($log . "�i�O�A$w_f_name $w_l_name ($w_cl $w_sex$w_no�f) �Q�k�]�F�I<br>") ;&SAVE;return ;}#�w�g仮以�H

if (length($dengon) > 0) {
	$log = ($log . "<font color=\"lime\"><b>$f_name $l_name ($cl $sex$no�f)�u$dengon�v</b></font><br>") ;
	$w_log = ($w_log . "<font color=\"lime\"><b>$hour:$min:$sec $f_name $l_name ($cl $sex$no�f)�u$dengon�v</b></font><br>") ;
}

&WEPTREAT($w_name, $w_kind, $wtai, $l_name, $w_l_name, "ю聖", "PC") ;
if ($dice1 < $mei) {	#ю聖Θ�\

	$result = ($att_p*$wk) - $def_n;
	$result /= 2 ;
	$result += rand($result);

	&DEFTREAT($w_kind, "NPC") ;
	$result = int($result * $pnt) ;

	if ($result <= 0) {$result = 1} ;
	$log = ($log . "�@�@<font color=\"red\"><b>$result ���� $hakaiinf3 $kega3 極�`</b></font>�I<br>") ;

	$w_hit -= $result;
	$w_btai--;
	if ($w_btai <= 0) { $w_bou = "ず��<>DN"; $w_bdef=0; $w_btai="】"; }

	$wep = $wep_2; $watt = $watt_2; $wtai = $wtai_2; $w_inf = $w_inf_2 ;
#�g島�a-�曚v
	$expup = int(($w_level - $level)/5);if ($expup <1){$expup = 1;}if($w_hit < 1){$expup += 1;}$exp += $expup;

} else {$kega3="";$log = ($log . "�i�O�A�Q宋�}�F�I<br>") ;}

if($w_hit <= 0){&DEATH2;}#篠�困`�H
elsif((rand(10) < 5)&&($w_ousen !~ /�v潜�M��|�k�`�査A/)){	#は聖

	if (($weps eq $weps2)||($weps2 eq "M")) {  #�Z託�@匙�H

		&WEPTREAT($w_name2, $w_kind2,  $w_wtai, $w_l_name, $l_name, "は聖", "NPC") ;

		if ($dice2 < $mei2) {   #ю聖Θ�\
			$result2 = ($att_n*$wk) - $def_p;
			$result2 /= 2 ;
			$result2 += rand($result2);

			&DEFTREAT($w_kind2, "PC") ;
			$result2 = int($result2 * $pnt) ;

			if ($result2 <= 0) {$result2 = 1 ;}
			$log = ($log . "�@�@<font color=\"red\"><b>$result2 ���� $kega2 極�`</b></font>�I<br>") ;

			$btai--;$hit -= $result2;

			if ($btai <= 0) { $bou = "ず��<>DN"; $bdef=0; $btai="】"; }

			if ($hit <=0) {&DEATH;}#�困`�H
			else {$log = ($log . "$w_l_name �k�]�F...�C<br>") ;}#�k�`
			$w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 菖茜�G$f_name $l_name ($cl $sex$no�f) ю�G$result2 �Q�G$result $hakaiinf2 $kega3 </b></font><br>") ;
			$w_wep = $w_wep_2; $w_watt = $w_watt_2; $w_wtai = $w_wtai_2; $inf = $inf_2 ;
#�g島�a-篠�H
	$expup = int(($level - $w_level)/5);if ($expup <1){$expup = 1;}if($hit < 1){$expup += 1;}$w_exp += $expup;
		} else {
			$w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 菖茜�G$f_name $l_name ($cl $sex$no�f) �Q�G$result $kega3 </b></font><br>") ;
			$log = ($log . "�@�@�i�O�A�d�v�@�vぇ孜宋�}�F�I<br>") ;
		}
		#�Z捷����
		if (($w_kind2 =~ /G|A/) && ($w_wtai > 0)) {$w_wtai--; if ($w_wtai <= 0) {$w_wtai = 0 ;}}#択�P�g�H
		elsif ($w_kind2 =~ /C|D/) {$w_wtai--; if ($w_wtai <= 0) { $w_wep ="�鼎�<>WP"; $w_watt=0; $w_wtai="】"; }}
		elsif (($w_kind2 =~ /N/) && (int(rand(5)) eq 0)) {$w_watt -= int(rand(2)+1) ; if ($w_watt <= 0) { $w_wep ="�鼎�<>WP"; $w_watt=0; $w_wtai="】"; }}

	} else {
		$log = ($log . "$w_l_name ぃ�爐論察I<br>　$w_l_name �k�]�F...�C<br>") ;
		$w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 茜菖�G$f_name $l_name ($cl $sex$no�f) �Q�G$result $hakaiinf2 $kega3 </b></font><br>") ;
	}
}else{	#�k�]
	$log = ($log . "$w_l_name �k�]�F...�C<br>") ;
	$w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 菖茜�G$f_name $l_name ($cl $sex$no�f) �Q�G$result $hakaiinf2 $kega3 </b></font><br>");
	if($w_ousen eq "�k�]�査A"){#�k�]悼�A�朧憤j宋
		($ara[0],$ara[1],$ara[2],$ara[3],$ara[4],$ara[5],$ara[6],$ara[7],$ara[8],$ara[9],$ara[10],$ara[11],$ara[12],$ara[13],$ara[14],$ara[15],$ara[16],$ara[17],$ara[18],$ara[19],$ara[20],$ara[21]) = split(/,/, $arealist[4]);
		$w_pls = $ara[$ar + int(rand(21 - $ar)) + 1];
		$w_log = ($w_log . "<font color=\"lime\"><b>$place[$w_pls]�w�g託�}�F�C</b></font><br>");
	}
}
#�Z捷����
if (($w_kind =~ /G|A/) && ($wtai > 0)) {$wtai--; if ($wtai <= 0) { $wtai = 0 ; }}#択�P�g�H
elsif ($w_kind =~ /C|D/) {$wtai--; if ($wtai <= 0) { $wep ="�鼎�<>WP"; $watt=0; $wtai="】"; }}
elsif (($w_kind =~ /N/) && (int(rand(5)) eq 0)) {$watt -= int(rand(2)+1) ; if ($watt <= 0) { $wep ="�鼎�<>WP"; $watt=0; $wtai="】"; }}

&LVUPCHK();

$w_bid = $id ;
$bid = $w_id ;

&SAVE;
&SAVE2;
}
#==================#
# ― �瓰隘霎山B�z  #
#==================#
sub ATTACK2 {
$kega2 = "" ; $kega3 = "" ;
$hakaiinf2 = ""; $hakaiinf3 = "";

if ($w_hit <= 0) {&ERROR("ぃタ訣�X維","no hit","attack-ATTACK2") ;}

local($result) = 0 ;
local($result2) = 0 ;
local($i) = 0 ;
local($dice1) = int(rand(100)) ;
local($dice2) = int(rand(100)) ;
($w_name,$w_kind) = split(/<>/, $wep);
($w_name2,$w_kind2) = split(/<>/, $w_wep);

&TACTGET; &TACTGET2;	#芋セ�羂�

#悉�饐�
if (($wep =~ /G|A/) && ($wtai == 0)) {$att_p = (($watt/10) + $att) * $atp ;}
else {$att_p = ($watt + $att) * $atp ;}
local($ball) = $def + $bdef + $bdef_h + $bdef_a + $bdef_f ;
if ($item[5] =~ /AD/) {$ball += $eff[5];} #庫喉┥�@�磧H
$def_p = $ball * $dfp ;

#篠
if (($w_wep =~ /G|A/) && ($w_wtai == 0)) {$att_n = (($w_watt/10) + $w_att) * $atn ;}
else {$att_n = ($w_watt + $w_att) * $atn ;}
local($ball2) = $w_def + $w_bdef + $w_bdef_h + $w_bdef_a + $w_bdef_f ;
if ($w_item[5] =~ /AD/) {$ball += $w_eff[5];} #庫喉┥�@�磧H
$def_n = $ball2 * $dfn ;

&BLOG_CK;
&EN_KAIFUKU;

$Command="BATTLE";

$log = ($log . "$w_f_name $w_l_name ($w_cl $w_sex$w_no�f) <BR>�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�雉M擢聖�L�咫I<br>") ;

&WEPTREAT($w_name2, $w_kind2,  $w_wtai, $w_l_name, $l_name, "ю聖", "NPC") ;
if ($dice2 < $me2) {	#ю聖Θ�\

	$result = ($att_n*$wk) - $def_p;
	$result /= 2 ;
	$result += rand($result);
	$result = int($result) ;

	&DEFTREAT($w_kind2, "PC") ;
	$result = int($result * $pnt) ;

	if ($result <= 0) {$result = 1 ;}
	$log = ($log . "�@�@<font color=\"red\"><b>$result ���� $kega2 極�`</b>�I</font><br>") ;

	$hit -= $result;
	$btai--;

	if ($btai <= 0) { $bou = "ず��<>DN"; $bdef=0; $btai="】"; }
	$w_wep = $w_wep_2; $w_watt = $w_watt_2; $w_wtai = $w_wtai_2; $inf = $inf_2 ;
	($w_name2,$w_kind2) = split(/<>/, $w_wep);
#�g島�a-篠
	$expup = int(($level - $w_level)/5);if ($expup <1){$expup = 1;}if($hit < 1){$expup += 1;}$w_exp += $expup;
} else {$log = ($log . "�@�@�i�O�A�d�v�@�vぇ孜宋�}�F�I<br>") ;}

if ($hit <= 0) {&DEATH;}#�困`�H
elsif (rand(10) <5) { #は聖

	if ($weps eq $weps2) {

		&WEPTREAT($w_name, $w_kind,  $wtai, $l_name, $w_l_name, "は聖", "PC") ;
		if ($dice1 < $mei) {	#ю聖Θ�\

			$result2 = ($att_p*$wk) - $def_n;
			$result2 /= 2 ;
			$result2 += rand($result2);
			$result2 = int($result2) ;

			&DEFTREAT($w_kind, "NPC") ;
			$result2 = int($result2 * $pnt) ;

			if ($result2 <= 0) {$result2 = 1 ;}
			$log = ($log . "�@�@<font color=\"red\"><b>$result2 ���� $hakaiinf3 $kega3 極�`</b>�I</font><br>") ;

			$w_hit -= $result2;
			$w_btai--;

			if ($w_btai <= 0) { $w_bou = "ず��<>DN"; $w_bdef=0; $w_btai="】"; }

			if ($w_hit <=0) {&DEATH2;}#�困`�H
			else {$log = ($log . "�@$l_name �k�]�F...�C<br>") ;}#�k�`

			$w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 菖茜�G$f_name $l_name ($cl $sex$no�f) ю�G$result �Q�G$result2 $hakaiinf2 $kega3 </b></font><br>") ;
			$wep = $wep_2; $watt = $watt_2; $wtai = $wtai_2; $w_inf = $w_inf_2 ;
			($w_name,$w_kind) = split(/<>/, $wep);
#�g島�a-�曚�
	$expup = int(($w_level - $level)/5);if ($expup <1){$expup = 1;}if($w_hit < 1){$expup += 1;}$exp += $expup;
		} else {
			$w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 菖茜�G$f_name $l_name ($cl $sex$no�f) ю�G$result $hakaiinf2 </b></font><br>") ;
			$log = ($log . "�@�i�O�A�Q宋�}�F�I<br>") ;
		}
		#�Z捷����
		if (($w_kind =~ /G|A/) && ($wtai > 0)) {$wtai--; if ($wtai <= 0) { $wtai = 0 ; }}#択�P�g�H
		elsif ($w_kind =~ /C|D/) {$wtai--; if ($wtai <= 0) { $wep ="�鼎�<>WP"; $watt=0; $wtai="】"; }}
		elsif (($w_kind =~ /N/) && (int(rand(5)) eq 0)) {$watt -= int(rand(2)+1) ; if ($watt <= 0) { $wep ="�鼎�<>WP"; $watt=0; $wtai="】"; }}
	} else {
		$log = ($log . "$l_name ぃ�爐論察I<br> $l_name �k�]�F...�C<br>") ;
		$w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 菖茜�G$f_name $l_name ($cl $sex$no�f) ю�G$result $hakaiinf2 $kega3 </b></font><br>") ;
	}
}else{	#�k�`
	$log = ($log . "$w_l_name �k┼�F...�C<br>") ;
	$w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec 菖茜�G$f_name $l_name ($cl $sex$no�f) �Q�G$result $hakaiinf2 $kega3 </b></font><br>");
	if($w_ousen eq "�k�]�査A"){#�k�]悼�A�朧憤j宋
		($ara[0],$ara[1],$ara[2],$ara[3],$ara[4],$ara[5],$ara[6],$ara[7],$ara[8],$ara[9],$ara[10],$ara[11],$ara[12],$ara[13],$ara[14],$ara[15],$ara[16],$ara[17],$ara[18],$ara[19],$ara[20],$ara[21]) = split(/,/, $arealist[4]);
		$w_pls = $ara[$ar + int(rand(21 - $ar)) + 1];
		$w_log = ($w_log . "<font color=\"lime\"><b>$place[$w_pls]�w�g託�}�F�C</b></font><br>");
	}
}
#�Z捷����
if (($w_kind2 =~ /G|A/) && ($w_wtai > 0)) {$w_wtai--; if ($w_wtai <= 0) {$w_wtai = 0 ;}}#択�P�g�H
elsif ($w_kind2 =~ /C|D/) {$w_wtai--; if ($w_wtai <= 0) { $w_wep ="�鼎�<>WP"; $w_watt=0; $w_wtai="】"; }}
elsif (($w_kind2 =~ /N/) && (int(rand(5)) eq 0)) {$w_watt -= int(rand(2)+1) ; if ($w_watt <= 0) { $w_wep ="�鼎�<>WP"; $w_watt=0; $w_wtai="】"; }}

&LVUPCHK();

&SAVE;
&SAVE2;
}
#==================#
# ― �Z捷寵�O�B�z  #
#==================#
sub WEPTREAT {

local($wname)	= @_[0];#�Z捷
local($wkind)	= @_[1];#�Z捷
local($wwtai)	= @_[2];#柴�q
local($pn)		= @_[3];#ю聖�巳W
local($nn)		= @_[4];#┥�s�巳W
local($ind)		= @_[5];#ю聖寵�O (ю聖/は聖)
local($attman)	= @_[6];#ю聖�� (PC/NPC)

local($dice3) = int(rand(100));	#極1
local($dice4) = int(rand(4));	#極2
local($dice5) = int(rand(100));	#�}�a�H

local($kega)	= 0;
local($kegainf)	= "";
local($k_work)	= "";
local($hakai)	= 0;

if ((($wkind =~ /B/)||(($wkind =~ /G|A/)&&($wwtai eq 0)))&&($wname ne "�鼎�")){#諌肝�A�l�u択�A�b�}
	$log = ($log . "$pn �� $ind�I<BR>�@$wname 灼ゴ $nn�I<BR>");
	if ($attman eq "PC") {$wp++;$wk=$wp;} else {$w_wp++;$wk=$w_wp;}
	$kega = 15 ;$kegainf = "�Y誼" ;			#��極�v�A極�單薊�
	$hakai = 2 ;		#�}�a�v
} elsif ($wkind =~ /C/) {			#щ�t
	$log = ($log . "$pn �� $ind�I<BR>�@$wname �V吸 $nn щ�Y�I<BR>");
	if ($attman eq "PC") {$wc++;$wk=$wc;} else {$w_wc++;$wk=$w_wc;}
	$kega = 15 ;$kegainf = "�Y誼" ;			#��極�v�A極�單薊�
	$hakai = 0 ;		#�}�a�v
} elsif ($wkind =~ /D/) {			#�z�t
	$log = ($log . "$pn �� $ind�I<BR>�@$wname �V吸 $nn щ�Y�I<BR>");
	if ($attman eq "PC") {$wd++;$wk=$wd;} else {$w_wd++;$wk=$w_wd;}
	$kega = 15 ;$kegainf = "�Y誼誼━" ;		#��極�v�A極�單薊�
	$hakai = 0 ;		#�}�a�v
} elsif ($wkind =~ /G/) {			#択�t
	$log = ($log . "$pn �� $ind�I<BR>�@$wname �V吸 $nn �o�ァI<BR>");
	if ($attman eq "PC") {$wg++;$wk=$wg;$ps=$pls;} else {$w_wg++;$wk=$w_wg;$ps=$w_pls;}
	$kega = 25 ; $kegainf = "�Y誼検━" ;	#��極�v�A極�單薊�
	$hakai = 1 ;		#�}�a�v
	if ($wkind !~ /S/){#�}択�n�紀`
		open(DB,"$gun_log_file");seek(DB,0,0); @gunlog=<DB>;close(DB);
		$gunlog[0] = "$now,$place[$ps],$id,$w_id,\n";
		open(DB,">$gun_log_file"); seek(DB,0,0); print DB @gunlog; close(DB);
	}
} elsif ($wkind =~ /K/) {			#�C�t
	$log = ($log . "$pn �� $ind�I<BR>�@$wname �襪F $nn�I <BR>");
	if ($attman eq "PC") {$ws++;$wk=$ws;} else {$w_ws++;$wk=$w_ws;}
	$kega = 25 ; $kegainf = "�Y誼検━" ;	#��極�v�A極�單薊�
	$hakai = 2 ;		#�}�a�v
} elsif ($wkind =~ /P/) {			#灼�t
	$log = ($log . "$pn �� $ind！<BR>�@$wname 灼ゴ $nn�I<BR>");
	if ($attman eq "PC") {$wp++;$wk=$wp;} else {$w_wp++;$wk=$w_wp;}
	$kega = 0 ; $kegainf = "" ;				#��極�v�A極�單薊�
	$hakai = 0 ;		#�}�a�v
} else {							#�筌�
	$log = ($log . "$pn �� $ind�I<BR>�@$wname ю聖 $nn�I<BR>");
	if ($attman eq "PC") {$wp++;$wk=$wp;} else {$w_wp++;$wk=$w_wp;}
	$kega = 0 ; $kegainf = "" ;				#��極�v�A極�單薊�
	$hakai = 0 ;		#�}�a�v
}

$wk = int($wk/$BASE) ;
if($wk == 0){$wk = 0.9;}elsif($wk == 1){$wk = 0.95;}elsif($wk == 2){$wk = 1.0;}elsif($wk == 3){$wk = 1.05;}elsif($wk == 4){$wk = 1.1;}else{$wk = 1.15;}
#刻も�H�曚v�H
if ($attman eq "PC") {$wep_2 = $wep; $watt_2 = $watt; $wtai_2 = $wtai ;$w_inf_2 = $w_inf ;}
else {$w_wep_2 = $w_wep; $w_watt_2 = $w_watt; $w_wtai_2 = $w_wtai ;$inf_2 = $inf ;}

# �Z捷�}�a
if ($dice5 < $hakai) {  #�}�a�H
	if ($attman eq "PC") {$wep_2 = "�鼎�<>WP"; $watt_2 = 0 ; $wtai_2 = "】" ;$hakaiinf3 = "�Z捷�l極�I" ;}#PC
	else {$w_wep_2 = "�鼎�<>WP"; $w_watt_2 = 0 ; $w_wtai_2 = "】" ;$hakaiinf2 = "�Z捷�l極�I" ;}
} else {$hakaiinf2 = "" ;$hakaiinf3 = "" ;}

# ��極�B�z
if ($dice3 < $kega) {
	if	  (($dice4 eq 0) && ($kegainf =~ /�Y/)) {$k_work = "�Y" ;}#�Y
	elsif (($dice4 eq 1) && ($kegainf =~ /誼/)) {$k_work = "誼" ;}#誼
	elsif (($dice4 eq 2) && ($kegainf =~ /検/)) {$k_work = "検" ;}#検
	elsif (($dice4 eq 3) && ($kegainf =~ /━/)) {$k_work = "━" ;}#━
	else {return ;}

	if ($attman eq "PC") {  #PC
		if ((($w_item[5] =~ /AD/)||($w_bou =~ /<>DB/)) && ($k_work eq "検")) {	#検�H
			if($w_item[5] =~ /AD/){$w_itai[5] --; if ($w_itai[5] <= 0) {$w_item[5]="�L"; $w_eff[5]=$w_itai[5]=0;}}
			else{$w_btai --; if ($w_btai <= 0) { $w_bou = "ず��<>DN"; $w_bdef=0; $w_btai="】"; }}
			return ;
		}
		elsif (($w_bou_h =~ /<>DH/) && ($k_work eq "�Y")) {$w_btai_h --; if ($w_btai_h <= 0) {$w_bou_h="�L"; $w_bdef_h=$w_btai_h=0;}return ;}#�Y�H
		elsif (($w_bou_f =~ /<>DF/) && ($k_work eq "━")) {$w_btai_f --; if ($w_btai_f <= 0) {$w_bou_f="�L"; $w_bdef_f=$w_btai_f=0;}return ;}#━�H
		elsif (($w_bou_a =~ /<>DA/) && ($k_work eq "誼")) {$w_btai_a --; if ($w_btai_a <= 0) {$w_bou_a="�L"; $w_bdef_a=$w_btai_a=0;}return ;}#誼�H
		else {$kega3 = ($k_work . "魁だ�t極");$w_inf_2 =~ s/$k_work//g ;$w_inf_2 = ($w_inf_2 . $k_work) ;}
	} else {
		if ((($item[5] =~ /AD/)||($bou =~ /<>DB/)) && ($k_work eq "検")) {	#検�H
			if($item[5] =~ /AD/){$itai[5] --; if ($itai[5] <= 0) {$item[5]="�L"; $eff[5]=$itai[5]=0;}}
			else{$btai --; if ($btai <= 0) { $bou = "ず��<>DN"; $bdef=0; $btai="】"; }}
			return ;
		}
		elsif (($bou_h =~ /<>DH/) && ($k_work eq "�Y")) {$btai_h --; if ($btai_h <= 0) {$bou_h="�L"; $bdef_h=$btai_h=0;}return ;}#�Y�H
		elsif (($bou_f =~ /<>DF/) && ($k_work eq "━")) {$btai_f --; if ($btai_f <= 0) {$bou_f="�L"; $bdef_f=$btai_f=0;}return ;}#━�H
		elsif (($bou_a =~ /<>DA/) && ($k_work eq "誼")) {$btai_a --; if ($btai_a <= 0) {$bou_a="�L"; $bdef_a=$btai_a=0;}return ;}#誼�H
		else {$kega2 = ($k_work . "魁だ�t極");$inf_2 =~ s/$k_work//g ;$inf_2 = ($inf_2 . $k_work) ;}
	}
}
}
#==================#
# ― �曚畝困`�B�z  #
#==================#
sub DEATH {
$hit = 0;$w_kill++;
$mem--;

$com = int(rand(6)) ;

$log = ($log . "<font color=\"red\"><b>$f_name $l_name ($cl $sex$no�f) �困`�C</b></font><br>") ;
if ($w_msg ne "") {$log = ($log . "<font color=\"lime\"><b>$w_f_name $w_l_name�y$w_msg�z</b></font><br>") ;}
$w_log = ($w_log . "<font color=\"yellow\"><b>$hour:$min:$sec $f_name $l_name ($cl $sex$no�f) �i�羮坩��A応�`�F�C�i丸�l $mem�H�j</b></font><br>") ;

local($b_limit) = ($battle_limit * 3) + 1;

if (($mem eq 1) && ($w_sts ne "NPC") && ($ar > $b_limit)){$w_inf = ($w_inf . "較") ;}

open(DB,"$gun_log_file");seek(DB,0,0); @gunlog=<DB>;close(DB);
$gunlog[1] = "$now,$place[$pls],$id,$w_id,\n";
open(DB,">$gun_log_file"); seek(DB,0,0); print DB @gunlog; close(DB);

#�困`刻柴(�O雀)
&LOGSAVE("DEATH2") ;
$death = $deth ;
}
#================#
# ― 篠�困`�B�z  #
#================#
sub DEATH2 {

$w_hit = 0;$kill++;
$wf = $w_id; #�s蹄捷�I魁棲刻
if (($w_cl ne "$BOSS")&&($w_cl ne "$ZAKO")){$mem--;}

$w_com = int(rand(6)) ;
$log = ($log . "<font color=\"red\"><b>$w_f_name $w_l_name ($w_cl $w_sex$w_no�f) 応�`�C�i丸�l$mem�H�j</b></font><br>") ;

if (length($w_dmes) > 1) {$log = ($log . "<font color=\"yellow\"><b>$w_f_name $w_l_name�y$w_dmes�z</b></font><br>") ;}
if (length($msg) > 1) {$log = ($log . "<font color=\"lime\"><b>$f_name $l_name�y$msg�z</b></font><br>") ;}

local($b_limit) = ($battle_limit * 3) + 1;
if (($mem == 1)&& ($ar > $b_limit)) {$inf = ($inf . "較") ;}

open(DB,"$gun_log_file");seek(DB,0,0); @gunlog=<DB>;close(DB);
$gunlog[1] = "$now,$place[$pls],$id,$w_id,\n";
open(DB,">$gun_log_file"); seek(DB,0,0); print DB @gunlog; close(DB);

#�困`刻柴(�O雀)
&LOGSAVE("DEATH3") ;

$Command = "BATTLE2" ;
$w_death = $deth ;
$w_bid = "";

}
#==============#
# ― �k�`�B�z  #
#==============#
sub RUNAWAY {$log = ($log . "$l_name ���t�k┼�F�C<BR>") ;$Command = "MAIN";}
#==================#
# ― ┥�禳悋O�B�z  #
#==================#
sub DEFTREAT {

local($wkind)	= @_[0] ;#�Z捷斎�O
local($defman)	= @_[1] ;#┥�s絢(PC/NPC)

local($p_up) = 1.5 ;
local($p_down) = 0.5 ;

if ($defman eq "PC") {  #PC?
	local($b_name,$b_kind) = split(/<>/, $bou);
	local($b_name_h,$b_kind_h) = split(/<>/, $bou_h);
	local($b_name_f,$b_kind_f) = split(/<>/, $bou_f);
	local($b_name_a,$b_kind_a) = split(/<>/, $bou_a);
	local($b_name_i,$b_kind_i) = split(/<>/, $item[5]);
} else {
	local($b_name,$b_kind) = split(/<>/, $w_bou);
	local($b_name_h,$b_kind_h) = split(/<>/, $w_bou_h);
	local($b_name_f,$b_kind_f) = split(/<>/, $w_bou_f);
	local($b_name_a,$b_kind_a) = split(/<>/, $w_bou_a);
	local($b_name_i,$b_kind_i) = split(/<>/, $w_item[5]);
}

if (($wkind eq "WG") && ($b_kind_i eq "ADB")) {$pnt = $p_down ;}#択＠┥�u
elsif (($wkind eq "WG") && ($b_kind_h eq "DH")) {$pnt = $p_up ;}#択＠�Y
elsif (($wkind eq "WN") && ($b_kind eq "DBK")) {$pnt = $p_down ;}#悦＠題
elsif (($wkind eq "WN") && ($b_kind_i eq "ADB")) {$pnt = $p_up ;}#悦＠┥�u
elsif ((($wkind eq "WB")||($wkind eq "WGB")||($wkind eq "WAB")) && ($b_kind_h eq "DH")) {$pnt = $p_down ;}#灼＠�Y
elsif ((($wkind eq "WB")||($wkind eq "WGB")||($wkind eq "WAB")) && ($b_kind =~ /DBA/)) {$pnt = $p_up ;}#灼＠�Zヒ
elsif (($wkind eq "WS") && ($b_kind =~ /DBA/)) {$pnt = $p_down ;}#�襦��Zヒ
elsif (($wkind eq "WS") && ($b_kind =~ /DBK/)) {$pnt = $p_up ;}#�襦�題
else {$pnt = 1.0 ;}
}
#======================#
# ― 汽�鉄�ど�B�z�@�@  #
#======================#
sub LVUPCHK {
if (($exp >= int($level*$baseexp+(($level-1)*$baseexp)))&&($hit > 0)) { #汽�鉄�ど
	&lvuprand;$log = ($log . "汽�鉄�ど�F�C<br><font color=\"00FFFF\">�i悼�j+$lvuphit �iю�j+$lvupatt �i┥�j+$lvupdef</font>") ;
	$hit += $lvuphit ;$mhit += $lvuphit ; $att += $lvupatt; $def += $lvupdef; $level++;$sta += 50;if ($maxsta < $sta){$sta = $maxsta;};
}
if (($w_exp >= int($w_level*$baseexp+(($w_level-1)*$baseexp)))&&($w_hit > 0)) { #レベルアップ
	&lvuprand;$w_log = ($w_log . "汽�鉄�ど�F�C<br><font color=\"00FFFF\">�i悼�j+$lvuphit �iю�j+$lvupatt �i┥�j+$lvupdef</font>") ;
	$w_hit += $lvuphit ;$w_mhit += $lvuphit ; $w_att += $lvupdef; $w_def += $lvupatt; $w_level++;$w_sta += 50;if ($maxsta < $w_sta){$w_sta = $maxsta;};
}
}
#==============================#
# ― 汽�哲爐O�H穣苅ど�B�z�@�@  #
#==============================#
sub lvuprand {$lvuphit = int(rand(2) + 9);$lvupatt = int(rand(3) + 3);$lvupdef = int(rand(3) + 2);}
#======================#
# ― 篠�^�_�B�z 	   #
#======================#
sub EN_KAIFUKU{ #篠�^�_�B�z
$up = int(($now - $w_endtime) / (1 * $kaifuku_time));
if (($w_inf =~ /腹/)&&($w_ousen ne "�v潜�M��")) { $up = int($up / 2) ; }
if (($w_inf !~ /腹/)&&($w_ousen eq "�v潜�M��")) { $up = int($up * 2) ; }
if ($w_sts eq "採�v") {
	$w_sta += $up;
	if ($w_sta > $maxsta) { $w_sta = $maxsta; }
	$w_endtime = $now;
} elsif ($w_sts eq "�v潜") {
	if($kaifuku_rate == 0){$kaifuku_rate = 1;}
	$up = int($up / $kaifuku_rate);
	$w_hit += $up;
	if ($w_hit > $w_mhit) { $w_hit = $w_mhit; }
	$w_endtime = $now;
} elsif ($w_sts eq "�R�i") {
	$w_sta += $up;
	if ($w_sta > $maxsta) { $w_sta = $maxsta; }
	if($kaifuku_rate == 0){$kaifuku_rate = 1;}
	$up = int($up / $kaifuku_rate);
	$w_hit += $up;
	if ($w_hit > $w_mhit) { $w_hit = $w_mhit; }
	$w_endtime = $now;
}
}
#=============================#
# ― 篠�H菖茜�O雀�朧払R娃�B�z #
#=============================#
sub BLOG_CK{$log_len = length($w_log);if(($w_sts eq "NPC")&&($log_len > 500)){$w_log = "<font color=\"yellow\"><b>�朧払R娃</b></font><br>";}elsif($log_len > 2222) {$w_log = "<font color=\"yellow\"><b>$hour:$min:$sec 菖茜�^�X�O雀�朧払R娃�C</b></font><br>";}}
1;
