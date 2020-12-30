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
