FasdUAS 1.101.10   ��   ��    k             l     ��������  ��  ��        j     �� 	�� 0 
dialogtext 
dialogText 	 m      
 
 �    S h o w M e�g,N-v�N�x      l     ��������  ��  ��        h    
�� �� 0 showme showMe  k             l    	 ����  I    	�� ��
�� .sysodlogaskr        TEXT  o     ���� 0 
dialogtext 
dialogText��  ��  ��     ��  i         I      �������� 0 showsomething showSomething��  ��    I    �� ��
�� .sysodlogaskr        TEXT  m        �   ��f/�g,[��aN-v�N�N�YtVh��  ��        l     ��������  ��  ��        l     ��   !��      
run ShowMe    ! � " "  r u n   S h o w M e   # $ # l     �� % &��   %  showSomething() of ShowMe    & � ' ' 2 s h o w S o m e t h i n g ( )   o f   S h o w M e $  ( ) ( l     ��������  ��  ��   )  * + * l     ,���� , O      - . - k     / /  0 1 0 I   ������
�� .aevtoappnull  �   � ****��  ��   1  2�� 2 I    �������� 0 showsomething showSomething��  ��  ��   . o     ���� 0 showme showMe��  ��   +  3 4 3 l     ��������  ��  ��   4  5 6 5 l      �� 7 8��   7vp

on idle	beep 2	say "I am still here, baby, do not worry"	return 5end idleon quit	display dialog "���Ҫ�˳��𣿲�Ҫ������" buttons {"��Ҫ����??", "�����??"}	if button returned of result = "��Ҫ����??" then		continue quit	end ifend quit

tell application "Finder"	make new folder at desktop with properties {name:"testScript"}	try		make new folder at desktop with properties {name:"testScript"}	end tryend tell

set content to (display dialog "����" default answer "����")display alert "����" message text returned of content as informationalbeep 10delay 5say "Hello Azen, I am Narra. How are you?"
    8 � 9 9� 
 
 o n   i d l e  	 b e e p   2  	 s a y   " I   a m   s t i l l   h e r e ,   b a b y ,   d o   n o t   w o r r y "  	 r e t u r n   5  e n d   i d l e   o n   q u i t  	 d i s p l a y   d i a l o g   "wv���� Q�T�N��bN�T� "   b u t t o n s   { "N��O`N��=� " ,   "�O`v��=�H " }  	 i f   b u t t o n   r e t u r n e d   o f   r e s u l t   =   "N��O`N��=� "   t h e n  	 	 c o n t i n u e   q u i t  	 e n d   i f  e n d   q u i t 
 
 t e l l   a p p l i c a t i o n   " F i n d e r "  	 m a k e   n e w   f o l d e r   a t   d e s k t o p   w i t h   p r o p e r t i e s   { n a m e : " t e s t S c r i p t " }  	 t r y  	 	 m a k e   n e w   f o l d e r   a t   d e s k t o p   w i t h   p r o p e r t i e s   { n a m e : " t e s t S c r i p t " }  	 e n d   t r y  e n d   t e l l 
 
 s e t   c o n t e n t   t o   ( d i s p l a y   d i a l o g   "T�T� "   d e f a u l t   a n s w e r   "�Ջ� " )  d i s p l a y   a l e r t   "�fTJ "   m e s s a g e   t e x t   r e t u r n e d   o f   c o n t e n t   a s   i n f o r m a t i o n a l   b e e p   1 0  d e l a y   5  s a y   " H e l l o   A z e n ,   I   a m   N a r r a .   H o w   a r e   y o u ? " 
 6  :�� : l     ��������  ��  ��  ��       �� ; < = >��   ; �������� 0 
dialogtext 
dialogText�� 0 showme showMe
�� .aevtoappnull  �   � **** < � ? ? 
"  O`S�N� = ��    @�� 0 showme showMe @   A B C A ������ 0 showsomething showSomething
�� .aevtoappnull  �   � **** B �� ���� D E���� 0 showsomething showSomething��  ��   D   E  ��
�� .sysodlogaskr        TEXT�� �j  C �� F���� G H��
�� .aevtoappnull  �   � **** F k     	 I I  ����  ��  ��   G   H ��
�� .sysodlogaskr        TEXT�� 
b   j   > �� J���� K L��
�� .aevtoappnull  �   � **** J k      M M  *����  ��  ��   K   L ����
�� .aevtoappnull  �   � ****�� 0 showsomething showSomething�� b   *j  O*j+ Uascr  ��ޭ