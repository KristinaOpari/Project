# Project
ikub-info
Kristi - Kam akses


28/12/2020
-Krijimi i modelit UserRole ne menyre qe te krijojme lidhjen ndermjet Userave dhe Roles. Gjithashtu fillimi i perdorimit te serializers, ku kam krijuar serializers bazuar te modelet dhe po bej prova qe ti paraqis ne views. Ketu po kam veshtiersi ne menyren se si do implementohen ne views ku po shikoj menyra te ndryshme. 

29/12/2020
-Fillim i perdorimit te viewsets te django rest framework, specifikisht django modelviewsets dhe ndryshimi i urls.py duke u bazuar ne ndryshime te views, ku fillova te perdor router. Gjithashtu bera nje funksion te scripts ne menyre qe modeli Role te popullohet dhe duke pasur nje csv file. 

30/12/2020
-Bera override metoden destory ne UserViewSet ne menyre qe te mos behet delete totalisht si record por te behet soft delete duke ndryshaur vetem vleren e field is_active nga True duke e bere False. Gjithashtu u mora me leave management ku kam krijuar 2 serializers te modelit Leave, njeren per LeaveApply dhe tjeter per LeaveApprove dhe me pas duke krijuar dhe 2 viewsets per secilen. Te viewset LeaveApprove meqenese thjesht do aprovohet nje leje qe eshte kerkuar nga dikush thjesht do jene funksionale metodat retrieve e update ne menyre qe aprovuesi te vendose statusin eshte approved apo rejected dhe cili eshte ky aprovues. Se fundi u mora dhe me datetime field per periudhen e fillimit dhe mbarimit te lejes se kerkuar ku kam bere nje funksion @property qe gjen duration te lejes, nese eshte brenda dites ne ore e nese eshte ne dite te ndryshme ne dite. 
--Dua te filloj te merrem dhe te calendar qe shfaqen te ditet e lejes qe te behen disable fundjavat dhe ditet qe kane kaluar qe te mos jene si opsion per tu zgjedhur.

31/12/2020
-U mora me krijimin automatik te accountit te userit me emailin qe vendoset dhe nje default password, duke bere override metoden save te class User, ku behet fillimit save Useri qe krijohet por dhe krijohet nje record te tabela Account. Lexova dhe ne lidhje me dergimin e emailit ne momentin qe krijohet account ne menyre qe useri te beje aktivizimin e accountit ne sistem. 
--Po has nje problem ne lidhje me berjen save te password ne db jo si charField. Si mundet ta zgjidh kete problem ose ku mund te orinetohem?
--Gjithashtu ne lidhje me berjen disable te fundjavave ne kalendar akoma nuk kam gjetur nje zgjidhje.

05/01/2021
-Kam bere disa modifikme vetem ne lidhje me paraqitjen te disa modeleve, per shembull kur kemi te bejme me choice fields te shfaqet vlera dhe jo key. Gjithashtu jam marre me exprotimin ne excel file dhe pdf file te informacionit ne lidhje me userat dhe kerkesat per leje. Per excel file kam perdorur librarin django import-export dhe file resources.py nderkohe qe per pdf file kam perdorur html templates, ku do e modifikoj me vone qe te mund te paraqiten dhe si tabela.

06/01/2021
-Bera modifikime ne html files qe u perdoren per tu eksportuar ne pdf files ne lidhje me users dhe leaves, ku ne pdf files do te tregohen ne formatin e tabelave.
