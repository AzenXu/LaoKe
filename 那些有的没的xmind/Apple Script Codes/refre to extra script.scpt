FasdUAS 1.101.10   ��   ��    k             l     ����  r       	  b     	 
  
 l     ����  c         l     ����  I    �� ��
�� .earsffdralis        afdr  m     ��
�� afdrdesk��  ��  ��    m    ��
�� 
ctxt��  ��    m       �   & S c r i p t   t o   L o a d . s c p t 	 o      ���� 0 thepath thePath��  ��        l     ��������  ��  ��        l    ����  r        I   �� ��
�� .sysoloadscpt        file  4    �� 
�� 
file  o    ���� 0 thepath thePath��    o      ���� 0 	thescript 	theScript��  ��        l     ��������  ��  ��        l     ����   I   �� !��
�� .aevtoappnull  �   � **** ! n     " # " o    ���� 0 showme showMe # o    ���� 0 	thescript 	theScript��  ��  ��     $ % $ l   & &���� & n    & ' ( ' I   " &�������� 0 showsomething showSomething��  ��   ( n    " ) * ) o     "���� 0 showme showMe * o     ���� 0 	thescript 	theScript��  ��   %  + , + l     ��������  ��  ��   ,  - . - l  ' , /���� / r   ' , 0 1 0 m   ' ( 2 2 � 3 3 
"  O`S�N� 1 n       4 5 4 o   ) +���� 0 
dialogtext 
dialogText 5 o   ( )���� 0 	thescript 	theScript��  ��   .  6 7 6 l  - 4 8���� 8 I  - 4�� 9��
�� .aevtoappnull  �   � **** 9 n   - 0 : ; : o   . 0���� 0 showme showMe ; o   - .���� 0 	thescript 	theScript��  ��  ��   7  < = < l     ��������  ��  ��   =  > ? > l  5 A @���� @ I  5 A�� A B
�� .sysostornull��� ��� scpt A o   5 6���� 0 	thescript 	theScript B �� C D
�� 
fpth C 4   7 ;�� E
�� 
file E o   9 :���� 0 thepath thePath D �� F��
�� 
savo F m   < =��
�� boovtrue��  ��  ��   ?  G H G l     ��������  ��  ��   H  I�� I l     ��������  ��  ��  ��       �� J K L M����   J ��������
�� .aevtoappnull  �   � ****�� 0 thepath thePath�� 0 	thescript 	theScript��   K �� N���� O P��
�� .aevtoappnull  �   � **** N k     A Q Q   R R   S S   T T  $ U U  - V V  6 W W  >����  ��  ��   O   P ������ �������������� 2����������
�� afdrdesk
�� .earsffdralis        afdr
�� 
ctxt�� 0 thepath thePath
�� 
file
�� .sysoloadscpt        file�� 0 	thescript 	theScript�� 0 showme showMe
�� .aevtoappnull  �   � ****�� 0 showsomething showSomething�� 0 
dialogtext 
dialogText
�� 
fpth
�� 
savo�� 
�� .sysostornull��� ��� scpt�� B�j �&�%E�O*��/j E�O��,j 	O��,j+ 
O���,FO��,j 	O��*��/�e�  L � X X X N a r r a : U s e r s : A z e n : D e s k t o p : S c r i p t   t o   L o a d . s c p t M �� Y  Z��   Y k       [ [  \ ] \ l     ��������  ��  ��   ]  ^ _ ^ j     �� `�� 0 
dialogtext 
dialogText ` m      a a � b b  S h o w M e�g,N-v�N�x _  c d c l     ��������  ��  ��   d  e f e h    
�� g�� 0 showme showMe g k       h h  i j i l    	 k���� k I    	�� l��
�� .sysodlogaskr        TEXT l o     ���� 0 
dialogtext 
dialogText��  ��  ��   j  m�� m i      n o n I      �������� 0 showsomething showSomething��  ��   o I    �� p��
�� .sysodlogaskr        TEXT p m      q q � r r ��f/�g,[��aN-v�N�N�YtVh��  ��   f  s t s l     ��������  ��  ��   t  u v u l     �� w x��   w  
run ShowMe    x � y y  r u n   S h o w M e v  z { z l     �� | }��   |  showSomething() of ShowMe    } � ~ ~ 2 s h o w S o m e t h i n g ( )   o f   S h o w M e {   �  l     ��������  ��  ��   �  � � � l     ����� � O      � � � k     � �  � � � I   ����~
�� .aevtoappnull  �   � ****�  �~   �  ��} � I    �|�{�z�| 0 showsomething showSomething�{  �z  �}   � o     �y�y 0 showme showMe��  ��   �  � � � l     �x�w�v�x  �w  �v   �  � � � l      �u � ��u   �vp

on idle	beep 2	say "I am still here, baby, do not worry"	return 5end idleon quit	display dialog "���Ҫ�˳��𣿲�Ҫ������" buttons {"��Ҫ����??", "�����??"}	if button returned of result = "��Ҫ����??" then		continue quit	end ifend quit

tell application "Finder"	make new folder at desktop with properties {name:"testScript"}	try		make new folder at desktop with properties {name:"testScript"}	end tryend tell

set content to (display dialog "����" default answer "����")display alert "����" message text returned of content as informationalbeep 10delay 5say "Hello Azen, I am Narra. How are you?"
    � � � �� 
 
 o n   i d l e  	 b e e p   2  	 s a y   " I   a m   s t i l l   h e r e ,   b a b y ,   d o   n o t   w o r r y "  	 r e t u r n   5  e n d   i d l e   o n   q u i t  	 d i s p l a y   d i a l o g   "wv���� Q�T�N��bN�T� "   b u t t o n s   { "N��O`N��=� " ,   "�O`v��=�H " }  	 i f   b u t t o n   r e t u r n e d   o f   r e s u l t   =   "N��O`N��=� "   t h e n  	 	 c o n t i n u e   q u i t  	 e n d   i f  e n d   q u i t 
 
 t e l l   a p p l i c a t i o n   " F i n d e r "  	 m a k e   n e w   f o l d e r   a t   d e s k t o p   w i t h   p r o p e r t i e s   { n a m e : " t e s t S c r i p t " }  	 t r y  	 	 m a k e   n e w   f o l d e r   a t   d e s k t o p   w i t h   p r o p e r t i e s   { n a m e : " t e s t S c r i p t " }  	 e n d   t r y  e n d   t e l l 
 
 s e t   c o n t e n t   t o   ( d i s p l a y   d i a l o g   "T�T� "   d e f a u l t   a n s w e r   "�Ջ� " )  d i s p l a y   a l e r t   "�fTJ "   m e s s a g e   t e x t   r e t u r n e d   o f   c o n t e n t   a s   i n f o r m a t i o n a l   b e e p   1 0  d e l a y   5  s a y   " H e l l o   A z e n ,   I   a m   N a r r a .   H o w   a r e   y o u ? " 
 �  ��t � l     �s�r�q�s  �r  �q  �t   Z �p � 2 � ��p   � �o�n�m�o 0 
dialogtext 
dialogText�n 0 showme showMe
�m .aevtoappnull  �   � **** � �l g M ��l 0 showme showMe �  Z � � � � �k�j�k 0 showsomething showSomething
�j .aevtoappnull  �   � **** � �i o�h�g � ��f�i 0 showsomething showSomething�h  �g   �   �  q�e
�e .sysodlogaskr        TEXT�f �j  � �d ��c�b � ��a
�d .aevtoappnull  �   � **** � k     	 � �  i�`�`  �c  �b   �   � �_
�_ .sysodlogaskr        TEXT�a 
b   j   � �^ ��]�\ � ��[
�^ .aevtoappnull  �   � **** � k      � �  ��Z�Z  �]  �\   �   � �Y�X
�Y .aevtoappnull  �   � ****�X 0 showsomething showSomething�[ b   *j  O*j+ U��   ascr  ��ޭ