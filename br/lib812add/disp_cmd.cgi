#ー―ー―ー―ー―ー―ー―ー―ー―ー―ー―ー
#― 	-    BR COMMAND DISPLAY    - 	 ―
#ー 									 ー
#― 		�@�@�l�{�任@蹄�@			 ―
#ー 									 ー
#― COMMAND		-	���O魁�@			 ―
#ー definition	-	�w�q魁				 ー
#―ー―ー―ー―ー―ー―ー―ー―ー―ー―ー―

#===================#
# ― ���O魁�@		#
#===================#
sub COMMAND {
local($i) = 0;
if ($sts =~ /採�v|�v潜|�R�i|�u較/) {
	$MESSENGER = "1";
	if ($sts eq "�v潜"){
		if($Command eq "HEAL"){$log = ($log . "�v潜極�w<BR>");}else{$log = ($log . "�v潜い�K<BR>");}
		$sts = "�v潜";print "�v潜い�K<BR><BR>";
		&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"HEAL2\" checked>�v潜</A><BR><BR>";
	} elsif ($sts eq "採�v"){
		if($Command eq "INN"){$log = ($log . "�y�L採�@�U<BR>");}else{$log = ($log . "採�vい�K<BR>");}
		$sts = "採�v";print "採�vい�K<BR><BR>";
		&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"INN2\" checked>採�v</A><BR><BR>";
	} elsif ($sts eq "�R�i"){
		if($Command eq "INNHEAL"){$log = ($log . "�R�iヰ��<BR>");}else{$log = ($log . "�R�iい�K<BR>");}
		$sts = "�R�i";print "�R�iい�K<BR><BR>";
		&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"INNHEAL2\" checked>�R�i</A><BR><BR>";
	} elsif ($sts eq "�u較"){
		print "<center><BR>可$WINNUM�^�u較��<BR>応�`柴-$kill<BR><BR><BR><INPUT type=\"submit\" name=\"Enter\" value=\"�隍^\"></center>";
		$MESSENGER = "0";return;
	}
	&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\">�隍^</A><BR><BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
	return;
}

if ((($Command eq '')||($Command eq "MAIN"))||(($Command eq "MOVE")&&($Command2 eq "MAIN"))||(($Command eq "ITMAIN")&&($Command3 eq "MAIN"))||(($Command eq "SPECIAL")&&($Command4 eq "MAIN"))) {   #MAIN
	$MESSENGER = "1";
	$log = ($log . "$jyulog$jyulog2$jyulog3�{�b�A�n�膽飽機K�C<br>") ;
	print "�i�罎飴髻H<BR><BR>";
	if ((($inf =~ /━/)&&($sta > 18))||(($inf !~ /━/)&&($club eq "外�W魁")&&($sta > 10))||(($inf !~ /━/)&&($sta > 13))){
		print "<INPUT type=\"radio\" name=\"Command\" value=\"MOVE\">";&AS;
		print "<select name=\"Command2\"><option value=\"MAIN\">― 仮以 ―<BR>";
			local(@kin_ar) = split(/,/, $arealist[2]);#р�Tゎ囲一�墾W恰�@�葦豆C�C
			if(($hackflg)||($sts eq "NPC")){$kinlist = "";} #濠�羝Tゎ囲一�@蹄�C
			else{for($k=0;$k<$ar;$k++){ $kinlist = ($kinlist . $kin_ar[$k]);}}#�{�b�左Tゎ囲一�l�[�C
			for ($j=0; $j<$#place+1; $j++) {
				if (($place[$j] ne $place[$pls])&&($kinlist !~ /$place[$j]/)) {print "<option value=\"MV$j\">$place[$j]($area[$j])<BR>";}
				elsif ($place[$j] eq $place[$pls]) {print "<option value=\"MAIN\"><--�{�b�豸m--><BR>";}
			}#�Tゎ囲一�B�z魁だ&�{�b�豸m
		print "</select></A><BR>";
	}
	if ($place[$pls] eq "だ��") {if (($hackflg eq 1)||($sts eq "NPC")) {$ok = 1;}}
	else {$ok = 0;if (($inf =~ /━/)&&($sta > 25)) {$ok = 1;} elsif (($club eq "バ�|魁")&&($sta > 15)) {$ok = 1;} elsif ($sta > 20) {$ok = 1;}}
	if ($ok){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"SEARCH\"> ― 唄�� ―&nbsp;</A><BR>";}
	print "<INPUT type=\"radio\" name=\"Command\" value=\"ITMAIN\">";&AS;
	print "<select name=\"Command3\"><option value=\"MAIN\">― �D�� ―<BR><option value=\"ITEM\">�D�礙魯痢P庫各<BR><option value=\"DEL\">�D�祓鷂m<BR><option value=\"SEIRI\">�D�秕祺z<BR><option value=\"GOUSEI\">�D�礒XΘ<BR>";
	if ($wep ne "�鼎�<>WP")	{print "<option value=\"WEPDEL\">娃�U庫各�Z捷<BR>";
							 print "<option value=\"WEPDEL2\">庫各�Z捷遠�m<BR>";}
	if ($bou_h ne "�L")	{print "<option value=\"BOUDELH\">娃�U�Y魁┥��<BR>";}
	if ($bou ne "ず��<>DN")	{print "<option value=\"BOUDELB\">娃�U�@悼┥��<BR>";}
	if ($bou_a ne "�L")	{print "<option value=\"BOUDELA\">娃�U誼魁┥��<BR>";}
	if ($bou_f ne "�L")	{print "<option value=\"BOUDELF\">娃�U━魁┥��<BR>";}
	if ($item[5] ne "�L")	{print "<option value=\"BOUDEL\">娃�U庫喉�~<BR>";}
	print "</select></A><BR><INPUT type=\"radio\" name=\"Command\" value=\"kaifuku\">";&AS;
	print "<select name=\"Command5\"><option value=\"MAIN\">― �^�_ ―<BR><option value=\"HEAL\">�@�v潜<BR><option value=\"INN\">�@採�v<BR>";
	if ($place[$pls] eq "�E潜��") {print "<option value=\"INNHEAL\">�@�R�i<BR>";}
	print "</select></A><BR><INPUT type=\"radio\" name=\"Command\" value=\"SPECIAL\">";&AS;
	print "<select name=\"Command4\"><option value=\"MAIN\" selected>― �S�� ―<BR>";
	print "<option value=\"KOUDOU\">�@芋セよ�w<BR>";
	print "<option value=\"OUSEN\">�@棲菖よ�w<BR>";
	#print "<option value=\"WINCHG\">�@�f�Y�y怒��<BR>";
	if ($sta > 50){print "<option value=\"OUKYU\">�@棲�羆幸I<BR>";}
	print "<option value=\"TEAM\">�@�p箇<BR>";
	if (($club eq "�堂z魁" )&&($sta > 30)) { print "<option value=\"PSCHECK\">�@�r┌<BR>"; }
	for ($poi=0; $poi<5; $poi++){if ($item[$poi] eq "�r団<>Y") {print "<option value=\"POISON\">�@�r���V�J<BR>";last;}}
	for ($spi=0; $spi<5; $spi++){if ($item[$spi] eq "亭�a喚�n捷<>Y") {print "<option value=\"SPIICH\">�@喚�n捷�魯�<BR>";last;}}
	for ($paso=0; $paso<5; $paso++){if (($item[$paso] eq "仮以PC<>Y")&&($itai[$paso] >= 1)) {print "<option value=\"HACK\">＾Hacking＾<BR>";last;}}
	print "</select></A><BR>";
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq "ITMAIN")&&($Command3 eq "GET")){	#�D��
	local($chkflg) = -1;
	for ($i=0; $i<5; $i++) {if ($item[$i] eq "�L") {$chkflg = $i;last;}}#�店D�磧H
	if ($chkflg eq "-1"){
		$log = ($log . "�o�唸D�磴w�颪��U�C<br>メ閏���咫H<BR>");
		print "メ閏���咫H<BR><BR>";
		($in, $ik) = split(/<>/, $item_get);&AS;
		print "<INPUT type=\"radio\" name=\"Command\" value=\"ITEMDELNEW\" checked>$in/$eff_get/$itai_get</A><BR><BR>";
		for ($i=0; $i<5; $i++) {if ($item[$i] ne "�L") {($in, $ik) = split(/<>/, $item[$i]);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ITEMNEWXCG_$i\">$in/$eff[$i]/$itai[$i]</A><BR>";}}
	}else{
		print "�n�p�鶻B�z�o�唸D�磧H<BR><BR>";&AS;
		print "<INPUT type=\"radio\" name=\"Command\" value=\"ITEMDELNEW\" checked>泳遠</A><BR><BR>";&AS;
		print "<INPUT type=\"radio\" name=\"Command\" value=\"ITEMGETNEW\">醤</A><BR>";
	}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq "ITMAIN")&&($Command3 eq "ITEM")){	#�D��
	$log = ($log . "�n�颪Jぐ賜�K�C<BR>") ;
	print "ノぐ賜�H<BR><BR>";&AS;
	print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>�隍^</A><BR><BR>";
	for ($i=0; $i<5; $i++) {if ($item[$i] ne "�L") {($in, $ik) = split(/<>/, $item[$i]);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ITEM_$i\">$in/$eff[$i]/$itai[$i]</A><BR>";}}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq "ITMAIN")&&($Command3 eq "DEL")){	#�D�祓鷂m
	$log = ($log . "障�z�D�磴ぁK�C<BR>");
	print "メ閏ぐ賜�H<BR><BR>";&AS;
	print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>�隍^</A><BR><BR>";
	for ($i=0; $i<5; $i++) {if ($item[$i] ne "�L") {($in, $ik) = split(/<>/, $item[$i]);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"DEL_$i\">$in/$eff[$i]/$itai[$i]</A><BR>";}}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq "ITMAIN")&&($Command3 eq "SEIRI")){	#�D�秕祺z
	$log = ($log . "障�z�D�磴ぁK�C<BR>");
	print "�n障�Xぐ賜�H<BR><BR>";
	print "<select name=\"Command\">";
	print "<option value=\"MAIN\" selected>苛ゎ</option>";
	for ($i=0; $i<5; $i++) {if ($item[$i] ne "�L") {($in, $ik) = split(/<>/, $item[$i]);print "<option value=\"SEIRI_$i\">$in/$eff[$i]/$itai[$i]</option>";}}
	print "</select><BR><BR><select name=\"Command2\"><option value=\"MAIN\" selected>苛ゎ</option>";
	for ($i2=0; $i2<5; $i2++) {if ($item[$i2] ne "�L") {($in2, $ik2) = split(/<>/, $item[$i2]);print "<option value=\"SEIRI2_$i2\">$in2/$eff[$i2]/$itai[$i2]</option>";}}
	print "</select><BR><BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq "ITMAIN")&&($Command3 eq "GOUSEI")){	#�D�礒XΘ
	$log = ($log . "�{�b��Τ�昏F�茵A�n�XΘ�s�@�任飴魘棔H<BR>") ;
	print "�n�XΘぐ賜�H<BR><BR>";
	print "<select name=\"Command\"><option value=\"GOUSEI1_N\" selected>�XΘ1</option>" ;
	for ($i=0; $i<5; $i++) {if ($item[$i] ne "�L") {($in, $ik) = split(/<>/, $item[$i]);print "<option value=\"GOUSEI1_$i\">$in/$eff[$i]/$itai[$i]</option>";}}
	print "</select><BR><BR><select name=\"Command2\"><option value=\"GOUSEI2_N\" selected>�XΘ2</option>" ;
	for ($i2=0; $i2<5; $i2++) {if ($item[$i2] ne "�L") {($in2, $ik2) = split(/<>/, $item[$i2]);print "<option value=\"GOUSEI2_$i2\">$in2/$eff[$i2]/$itai[$i2]</option>";}}
	print "</select><BR><BR><select name=\"Command3\"><option value=\"GOUSEI3_N\" selected>�XΘ3</option>";
	for ($i3=0; $i3<5; $i3++) {if ($item[$i3] ne "�L") {($in3, $ik3) = split(/<>/, $item[$i3]);print "<option value=\"GOUSEI3_$i3\">$in3/$eff[$i3]/$itai[$i3]</option>";}}
	print "</select><BR><BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq SPECIAL)&&($Command4 eq "OUKYU")){	#棲�羈B�z
	$log = ($log . "�v潜極�w�K�C<BR>") ;
	print "�v潜�鶻B�H<BR><BR>";&AS;
	print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>�隍^</A><BR><BR>";
	if ($inf =~ /�Y/) {&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUK_0\">�Y</A><BR>"; }
	if ($inf =~ /誼/) {&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUK_1\">誼</A><BR>"; }
	if ($inf =~ /検/) {&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUK_2\">検</A><BR>"; }
	if ($inf =~ /━/) {&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUK_3\">━</A><BR>"; }
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq "SPECIAL")&&($Command4 eq "KOUDOU")){	#芋セよ�w
	$log = ($log . "σ�{芋セよ�w�K�C<BR>") ;
	print "出�M�w芋セよ�w�C<BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>�隍^</A><BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"KOU_0\">�q�`</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"KOU_1\">ю聖��鋸</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"KOU_2\">┥�s��鋸</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"KOU_3\">藻�K�羂�</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"KOU_4\">営�薦羂�</A><BR>";
	if($ar >= 7){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"KOU_5\">�s茜�羂�</A><BR>";}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq "SPECIAL")&&($Command4 eq "OUSEN")){	#棲菖よ�w
	$log = ($log . "σ�{棲菖よ�w�K�C<BR>") ;
	print "出�M�w棲菖よ�w�C<BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>�隍^</A><BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_0\">�q�`</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_1\">ю聖��鋸</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_2\">┥�s��鋸</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_3\">藻�K�羂�</A><BR>";
#&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_4\">唄�薦羂�</A><BR>";
#&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_5\">�s茜�羂�</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_6\">�v潜�M��</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"OUS_7\">�k�]�査A</A><BR>";
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif ($Command =~ /BATTLE0/){	#菖茜���O
	local($a,$wid) = split(/_/, $Command);
	$log = ($log . "┷賜�A�n�膽飽機K�C");$chk = "checked" ;
	print "圧ぐ賜�H<BR><BR>�V刻も�P�謬o�X�T�АG<BR><INPUT size=\"30\" type=\"text\" name=\"Dengon\" maxlength=\"64\"><BR><BR>";
	($w_name,$w_kind) = split(/<>/, $wep);
	if(($w_kind =~ /G/)&&($wtai > 0)){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WG_$wid\" $chk>�g聖($wg)</A><BR>"; $chk="";}
	if($w_kind =~ /K/){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WK_$wid\" $chk>悦(�C)($ws)</A><BR>"; $chk="";}
	if($w_kind =~ /C/){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WC_$wid\" $chk>щ�Y(щ)($wc)</A><BR>"; $chk="";}
	if($w_kind =~ /D/){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WD_$wid\" $chk>щ�Y(�z)($wd)</A><BR>"; $chk="";}
	if($w_kind =~ /P|B/){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WB_$wid\" $chk>灼ゴ(灼)($wp)</A><BR>"; $chk="";}
	if(($w_kind !~ /G|K|C|D|P|B/)&&(($w_kind =~ /G|A/)&&($wtai eq 0))){&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WB_$wid\" $chk>灼ゴ($wp)</A><BR>"; $chk="";}
	&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"RUNAWAY\">�k�`</A><BR><BR>";
	print "<INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif ($Command eq "ITEMJOUTO"){	#�D�秣狹�
	$log = ($log . "�D�秣狹����O�C<BR>");
	print "$w_cl$w_no�f $w_f_name $w_l_name<br>�@�@�@�@退統���唸D�磧H<INPUT type=\"hidden\" name=\"Command\" value=\"SEITO_$w_id\"><BR><BR>";
	print "<select name=\"Command2\"><option value=\"JO_MAIN\" selected>苛ゎ</option>";
	for ($i=0; $i<5; $i++) {if ($item[$i] ne "�L") {($in, $ik) = split(/<>/, $item[$i]);print "<option value=\"JO_$i\">$in/$eff[$i]/$itai[$i]<BR></option>";}}
	print "</select><BR><BR>����<BR><INPUT size=\"30\" type=\"text\" name=\"Dengon\" maxlength=\"64\"><BR><BR>";
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif ($Command eq "BATTLE2"){	#�D�祓姐�
	local($itno) = -1;
	for($i=0; $i<5; $i++){if($item[$i] eq "�L"){$itno = $i;}}
	print "砿┼ぐ賜�H<BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>�隍^</A><BR><BR>";
	print "<INPUT TYPE=\"HIDDEN\" NAME=\"Itno\" VALUE=\"$itno\"><INPUT TYPE=\"HIDDEN\" NAME=\"WId\" VALUE=\"$w_id\">";
	#�Z捷�勦��H
	if($w_wep !~ /�鼎�/){local($in, $ik) = split(/<>/, $w_wep);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_6\">$in/$w_watt/$w_wtai</A><BR>";}
	#┥�礬勦��H
	if($w_bou !~ /ず��/){local($in, $ik) = split(/<>/, $w_bou);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_7\">$in/$w_bdef/$w_btai</A><BR>";}
	#┥�礬勦��H
	if($w_bou_h !~ /�L/){local($in, $ik) = split(/<>/, $w_bou_h);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_8\">$in/$w_bdef_h/$w_btai_h</A><BR>";}
	#┥�礬勦��H
	if($w_bou_f !~ /�L/){local($in, $ik) = split(/<>/, $w_bou_f);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_9\">$in/$w_bdef_f/$w_btai_f</A><BR>";}
	#┥�礬勦��H
	if($w_bou_a !~ /�L/){local($in, $ik) = split(/<>/, $w_bou_a);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_10\">$in/$w_bdef_a/$w_btai_a</A><BR>";}
	#�D�礬勦��H
	for($i=0; $i<6; $i++){if ($w_item[$i] ne "�L"){local($in, $ik) = split(/<>/, $w_item[$i]);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_$i]\">$in/$w_eff[$i]/$w_itai[$i]</A><BR>";}}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif ($Command eq "DEATHGET") {  #�妖藕D�祓姐�
	local($itno) = -1;
	for ($i=0; $i<5; $i++) {if ($item[$i] eq "�L") {$itno = $i;}}
	print "�n砿┼ぐ賜�H<BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>�隍^</A><BR><BR>";
	print "<INPUT TYPE=\"HIDDEN\" NAME=\"Itno\" VALUE=\"$itno\"><INPUT TYPE=\"HIDDEN\" NAME=\"WId\" VALUE=\"$w_id\">";
	#�Z捷�勦��H
	if($w_wep !~ /�鼎�/){local($in, $ik) = split(/<>/, $w_wep);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_6\">$in/$w_watt/$w_wtai</A><BR>";}
	#┥�礬勦��H
	if($w_bou !~ /ず��/){local($in, $ik) = split(/<>/, $w_bou);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_7\">$in/$w_bdef/$w_btai</A><BR>";}
	#┥�礬勦��H
	if($w_bou_h !~ /�L/){local($in, $ik) = split(/<>/, $w_bou_h);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_8\">$in/$w_bdef_h/$w_btai_h</A><BR>";}
	#┥�礬勦��H
	if($w_bou_f !~ /�L/){local($in, $ik) = split(/<>/, $w_bou_f);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_9\">$in/$w_bdef_f/$w_btai_f</A><BR>";}
	#┥�礬勦��H
	if($w_bou_a !~ /�L/){local($in, $ik) = split(/<>/, $w_bou_a);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_10\">$in/$w_bdef_a/$w_btai_a</A><BR>";}
	#�D�礬勦��H
	for ($i=0; $i<6; $i++) {if ($w_item[$i] ne "�L") {local($in, $ik) = split(/<>/, $w_item[$i]);&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"GET_$i\">$in/$w_eff[$i]/$w_itai[$i]</A><BR>";}}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq SPECIAL)&&($Command4 eq "POISON")) {	#�r���V�J
	$log = ($log . "�p�G�V�M�o�哮r団�K�K�K�K�C<BR>") ;
&AS;print "�V�Jぐ賜�r���H<BR><BR><INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>�隍^</A><BR><BR>";
	for ($i=0; $i<5; $i++) {
		if ($item[$i] =~ /<>SH|<>HH|<>SD|<>HD/) {
			local($in, $ik) = split(/<>/, $item[$i]);
		&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"POI_$i\">$in/$eff[$i]/$itai[$i]</A><BR>";
		}
	}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq SPECIAL)&&($Command4 eq "PSCHECK")) {	#�r┌
	$log = ($log . "胡吸春�dΤ�SΤぐ賜�Q�V�J�K�C<BR>") ;
&AS;print "圧ぐ賜旗胡芹�H<BR><BR><INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>�隍^</A><BR><BR>";
	for ($i=0; $i<5; $i++) {
		if ($item[$i] =~ /<>SH|<>HH|<>SD|<>HD/) {
			local($in, $ik) = split(/<>/, $item[$i]);
		&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"PSC_$i\">$in/$eff[$i]/$itai[$i]</A><BR>";
		}
	}
	print "<BR><INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq SPECIAL)&&($Command4 eq "SPIICH")) { #亭�a喚�n捷�魯�
	$log = ($log . "�p�G�魯粒o�咫A�j�a棲袴泥┌�K<BR><BR>") ;
	print "�魯猟皹a喚�n捷�A�V��悼�H��暁�F�f�H�C";
	print "(殻�h20�咼�┐�r)<BR><BR>";
	print "<INPUT size=\"30\" type=\"text\" name=\"speech\"maxlength=\"50\"><BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"SPEAKER\">暁�F</A><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>苛ゎ</A><BR><BR>";
	print "<INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">\n";
#} elsif (($Command eq SPECIAL)&&($Command4 eq "WINCHG")) {	#�f�Y�y怒��
#	$log = ($log . "応�`�鼻A怒�鵙困`�肘困f�Y�y�C<BR>") ;
#	print "出翠�J�f�Y�y<BR>(殻�h32�咼�┐�r)<BR><BR>";
#	print "応�`�鼻G<BR><INPUT size=\"30\" type=\"text\" name=\"Message\" maxlength=\"64\" value=\"$msg\"><BR><BR>";
#	print "崇┘�G<BR><INPUT size=\"30\" type=\"text\" name=\"Message2\" maxlength=\"64\" value=\"$dmes\"><BR><BR>";
#	print "�N�蹈y�G<BR><INPUT size=\"30\" type=\"text\" name=\"Comment\" maxlength=\"64\" value=\"$com\"><BR><BR>";
#	print "<INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif (($Command eq SPECIAL)&&($Command4 eq "TEAM")) {	#兇ヮ
	$log = ($log . "�p箇�魂妣─P�[�J�P我託<BR>") ;
	print "出翠�J�p箇�W<BR>�@�@ �A�漫A�p�G我託<br>�@�@�@�@ 濁よ�N�A�SΤ猪�Y�C<BR>";
	print "(殻�h12�咼�┐�r)<BR><BR>";
	print "<INPUT size=\"30\" type=\"text\" name=\"teamID2\" maxlength=\"24\" value=\"$teamID\"><BR><BR><BR>";
	print "出翠�J�K�X�G<BR>(8�咼�┐�r�Hず)<BR><BR>";
	if (($teamID ne "")||($teamID ne "�L")){$teamPass2 = "ぃ怒�鶫艮！p"}else{$teamPass2 = "";}
	print "<INPUT size=\"30\" type=\"text\" name=\"teamPass2\" maxlength=\"16\" value=\"$teamPass2\"><BR><BR>";
	print "<INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} elsif ($Command eq USRSAVE) {							#ノめ柴証�O�s
	local($u_dat) = "$id,$password,$f_name,$l_name,$sex,$cl,$no,$endtime,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg,$sts,$pls,$kill,$icon,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],,$dmes,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com,$inf,$ousen,$seikaku,$sinri,$item_get,$eff_get,$itai_get,$teamID,$teamPass,$IP,\n" ;
	open(DB,">$u_save_dir$id$u_save_file"); seek(DB,0,0); print DB $u_dat; close(DB);
	$log = ($log . "タ�`�O雀飢�堯C<BR>") ;
&AS;print "<br><INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>�隍^</A><BR><BR>";
	print "<INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
} else {
	print "�i�罎飴髻H<BR><BR>";
&AS;print "<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>�隍^</A><BR><BR>";
	print "<INPUT type=\"submit\" name=\"Enter\" value=\"�M�w\">";
}

}
#===========#
# ― �w�q魁	#
#===========#
sub definition {
$up = int(($level*$baseexp)+(($level-1)*$baseexp)) ;
$levuprem = $up-$exp;
#Name Def & class
$full_name ="$f_name $l_name";$cln = "$cl $sex$no�f" ;
#�t極�aよ
$kega ="";$kegaimg ="";$condi = "<BR><BR>タ�`";$kegaa=0;
if (($sta <= "50")||($hit <= "50")){$condition="C";$condi = "<BR><BR>�`�N"}
if ($inf =~ /�Y/) {$kegaimg = ($kegaimg . "H");$kega = ($kega . "�Y ");$kegaa=1;}
if ($inf =~ /誼/) {$kegaimg = ($kegaimg . "A");$kega = ($kega . "誼 ");$kegaa=1;}
if ($inf =~ /検/) {$kegaimg = ($kegaimg . "B");$kega = ($kega . "検 ");$kegaa=1;}
if ($inf =~ /━/) {$kegaimg = ($kegaimg . "F");$kega = ($kega . "━ ");$kegaa=1;}
if ($kegaa){$condi = "<BR><BR>�t極";$condition="C";}
if ($inf =~ /�r/) {$condi = "<BR><BR>�r";$condition="P";}
if ($kega eq "")  {$kega = "�L" ;}
if (($sta <= "25")&&($hit <= "50")){$condition="D";$condi = "<BR><BR>諜�i"}
if ($kegaimg eq ""){$kegaimg = ($kegaimg . "OK");}
$kegaimg = ($kegaimg . ".jpg");
$kegaimg = "<IMG src=\"img/$kegaimg\" align=\"top\" border=\"0\" align=\"middle\">";
#Condition
if	 ($condition eq "C") {$CONDITION = "<EMBED src=\"$caution\" HEIGHT=70 width=140>";}
elsif($condition eq "D") {$CONDITION = "<EMBED src=\"$danger\" HEIGHT=70 width=140>";}
elsif($condition eq "P") {$CONDITION = "<EMBED src=\"$poison\" HEIGHT=70 width=140>";}
else {$CONDITION = "<EMBED src=\"$fine\" HEIGHT=70 width=140>";}
#get time
($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime($now);$hour = "0$hour" if ($hour < 10);$min = "0$min" if ($min < 10);  $month++;$year += 1900;$week = ('ら','る','��','��','れ','��','�g') [$wday];
#庫各 Def
($w_name,$w_kind) = split(/<>/, $wep);($b_name,$b_kind) = split(/<>/, $bou);($b_name_h,$b_kind_h) = split(/<>/, $bou_h);($b_name_f,$b_kind_f) = split(/<>/, $bou_f);($b_name_a,$b_kind_a) = split(/<>/, $bou_a);($b_name_i,$b_kind_i) = split(/<>/, $item[5]);
if (($w_kind =~ /G|A/) && ($wtai == 0)) {$watt_2 = int($watt/10) ;}else {$watt_2 = $watt ;}#諌肝 or �l�u択 or �b�}
$ball = $bdef + $bdef_h + $bdef_a + $bdef_f ;
if ($item[5] =~ /AD/) {$ball += $eff[5];} #庫喉┥�@�磧H
#Bar Def
$exp_bar1 = int($exp / $up * 100);$sta_bar1 = int($sta / $maxsta* 100);$hit_bar1 = int($hit / $mhit* 100);

if ($exp_bar1 > 100){$exp_bar1 = 100;}if ($sta_bar1 > 100){$sta_bar1 = 100;}if ($hit_bar1 > 100){$hit_bar1 = 100;}
$exp_bar2 = 100 - $exp_bar1;$sta_bar2 = 100 - $sta_bar1;$hit_bar2 = 100 - $hit_bar1;
$bar_exp1 = "<IMG src=\"$yellow\" width=\"$exp_bar2%\" height=\"5\" border=\"0\" align=\"middle\">";$bar_sta1 = "<IMG src=\"$red\" width=\"$sta_bar2%\" height=\"10\" border=\"0\" align=\"middle\">";$bar_hit1 = "<IMG src=\"$pink\" width=\"$hit_bar2%\" height=\"10\" border=\"0\" align=\"middle\">";$bar_exp2 = "<IMG src=\"$gold\" width=\"$exp_bar1%\" height=\"5\" border=\"0\" align=\"middle\">";$bar_sta2 = "<IMG src=\"$blue\" width=\"$sta_bar1%\" height=\"10\" border=\"0\" align=\"middle\">";$bar_hit2 = "<IMG src=\"$green\" width=\"$hit_bar1%\" height=\"10\" border=\"0\" align=\"middle\">";
if ($exp_bar2 eq 0){$bar_exp1 = "";}if ($sta_bar2 eq 0){$bar_sta1 = "";}if ($hit_bar2 eq 0){$bar_hit1 = "";}if ($exp_bar1 eq 0){$bar_exp2 = "";}if ($sta_bar1 eq 0){$bar_sta2 = "";}if ($hit_bar1 eq 0){$bar_hit2 = "";}
$bar_exp = "$bar_exp2$bar_exp1";$bar_sta = "$bar_sta2$bar_sta1";$bar_hit = "$bar_hit2$bar_hit1";
}

1;
