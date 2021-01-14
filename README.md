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

07/01/2021
-Jam marre me popullimin e tabeles holidays duke perdorur nje file csv holidays.csv nepermjet scriptit. Te ky file kam vendosur te gjithe festat zyrtare te Shqiperise. Pasi kam lexuar file dhe kam krijuar objektet, duke perdorur nje for loop kam kontrolluar per rastet kur festat bien dite te shtune ose te diele, ku e hena do te jete pushim. Gjithashtu dhe rastin  kur bie e shtune dhe e diele te dyja festa dhe eshte dhe e hena dhe e marta perseri pushim. Keshtu qe pas objekteve te krijuara nga leximi i holidays.csv jane krijuar dhe objete te tjera shtese per ditet e pushim te hene ose te marte. 

11/01/2021
-Sot u mora pak me modifikimin e modelit User duke e bere SystemUser qe te inherit nga AbstractUser, ku ka disa field vete nga inherit, por dhe shtova disa fields vete. Gjithashtu dhe modifikimet ne pjeset e tjera te projektit ku perdorej modeli User dhe fields qe kishte me pare, duke adaptuar me fields qe do te kete tani.

12/01/20212
-Kam shtuar nje model per UserManager sepse bera si USERNAME_FIELD te SystemUser model field-in e emailit dhe kam hequr fare si field ate te username-it. Ne kete model gjithashtu kam bere override metoden save ne menyre qe kur te behet save te dhenat per userin do te krijoje rekorde te UserRole table nese is_hr eshte true is_Employee eshte true dhe e njejta per is_Supervisor. Gjithashtu u mora me funksionin qe ne momentin qe aprovohet leja e nje user-i qe ka kerkuar leje per 1 dite ose me shume, te leave_days_available te zbritet numri i diteve qe do te jete me leje. Dhe te serializer.py kame bere disa modifikime vetem ne lidhje me paraqitjen e te dhenave te userave,lejeve etj. 

13/01/2021
-Bera nje ndryshim ne override te save method per userin qe te krijonte nje record te ri te UserRole vetem ne qofte se ai rekord nuk ekzisonte me pare. Me tej ne secilin viewset kam vendosur authenitcation classes ku e kam vendosur basic authentiaction qe ne momentin qe do aksesohet nje url duhet qe credentials te nje useri te merren dhe ne baze te userit te loguar do te behen veprimet. Per shembull ne momentin qe do te kerkohet leja user_id e tabeles Leave do te merret useri qe eshte i loguar ne sistem, per ta bere kete kam bere override metodat perform_create dhe perform_update aty ku nevojiteshin. Gjithashtu u mora me krijimin e nje view ne momentin qe useri do te ndryshoje passwordin. 
Po shikoj dhe opsionin qe useri te kerkoje reset-im te passwordit.

14/01/2021
-U mora me pjesen e permission ku krijova nje python file permissions.py ku krijova 3 custom permission isHr isEmployee dhe isSupervisor. Meqe kirjova keto permissions te viewsets te SystemUser dhe Leave ku duhet te kishim disa restrictions ne baze te rolit qe ka useri i loguar bera override metoden get_permissions si dhe metoden get_queryset. Per shembull ne momentin qe useri esht Hr queryset do i userave do te jene te gjithe userat, ndera ne momentin qe eshte supervisor queryset do te jene te gjithe userat qe i takojne atij departamenti ku current user eshte supervisor. Ndersa ne lidhje me permissions , ne momentin qe user do te jete Hr do te kete permission te krijoje nje user te ri, te updatoje userat, te shikoje gjithe listen e userave, te delete ke user deshiron. Ndersa nese eshte thjesht supervisor ose employee nuk ka te dreje te krijoje ose te beje update usera te tjere, vetem te shikoje te dhenat e tij(ne rastin e employee) dhe ne rastin e supervisor dhe te userave te tjera ne departament.  E njeja llogjike dhe per Leave Model me specifikimet e ketij modeli. 
