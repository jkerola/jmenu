# ruff: noqa


class MockResponse:
    def json(self):
        return get_json()


def mock_fetch_restaurant(*args, **kwargs):
    return MockResponse()


def mock_fetch_restaurant_fail():
    raise Exception("This is an error.")


def get_json():
    return [
        {
            "kitchenName": "Ravintola Mara",
            "kitchenId": 49,
            "address": "",
            "city": "",
            "email": "",
            "phone": "",
            "info": "",
            "menuTypes": [
                {
                    "menuTypeId": 31,
                    "menuTypeName": "Jälkiruoka",
                    "menus": [
                        {
                            "menuName": "Mara jälkiruoka (37-42)",
                            "menuAdditionalName": "BI 11.09.2023-20.10.2023",
                            "menuId": 4115,
                            "days": [
                                {
                                    "date": 20230913,
                                    "weekday": 3,
                                    "mealoptions": [
                                        {
                                            "name": "JÄLKIRUOKA",
                                            "orderNumber": 50,
                                            "id": 8,
                                            "menuItems": [
                                                {
                                                    "name": "Kookospannacotta",
                                                    "orderNumber": 1,
                                                    "portionSize": 100,
                                                    "diets": "",
                                                    "ingredients": "Valkoinen leivontasuklaa (Sokeri, kaakaovoi, täysMAITOjauhe, LAKTOOSI, VOIrasva, emulgointiaine (auringonkukkalesitiini, E476), vanilja-aromi. Saattaa sisältää pieniä määriä gluteenia sisältäviä viljoja, soijaa, kananmunaa, pähkinöitä ja maapähkinää.) (maito), Vispikerma (KERMA, stabilointiaine (karrageeni)) (Maito), Kookoskerma (Kookospähkinäuute (90 %), vesi), Tomusokeri (Sokeri ja perunatärkkelys 2%), Mansikka (mansikka (100 %)), Mustikka (pensasmustikka), Liivate (Liivatelehti. Ihmisravinnoksi tarkoitettu gelatiini. Valmistettu sian nahasta.), Valkolupiininverso (suomalainen valkolupiinin verso) (lupiini), Vaniljatanko (Vaniljatanko.)",
                                                }
                                            ],
                                        }
                                    ],
                                }
                            ],
                        }
                    ],
                },
                {
                    "menuTypeId": 51,
                    "menuTypeName": "Salad and soup",
                    "menus": [
                        {
                            "menuName": "Mara Salad & Soup (37-42)",
                            "menuAdditionalName": "BI 11.09.2023-20.10.2023",
                            "menuId": 4114,
                            "days": [
                                {
                                    "date": 20230913,
                                    "weekday": 3,
                                    "mealoptions": [
                                        {
                                            "name": "LOUNAS KEITTO",
                                            "orderNumber": 24,
                                            "id": 6,
                                            "menuItems": [
                                                {
                                                    "name": "Punajuurisosekeitto",
                                                    "orderNumber": 1,
                                                    "portionSize": 402,
                                                    "diets": "G, L, Mu, *",
                                                    "ingredients": "Vesi, Punajuuri (karbokuorittu punajuuri (100%)), Peruna (peruna, hapettumisenestoaine (NATRIUMDISULFIITTI)) (Rikkidioksidi), Ruokakerma, Sipuli (sipuli (Puola)), Punajuurikuutio mausteliemessä (Punajuuri, vesi, sokeri, happo (etikkahappo), säilöntäaine (kaliumsorbaatti), neilikka-aromi.), Vähäsuolainen kasvisliemijauhe (Suola, maltodekstriini, sipuli 10 %, luontainen aromi, palsternakka 5,2 %, porkkana 4,6 %, purjo 0,3 %. Kasvikset 20 %.), Suola (Ruokasuola ja paakkuuntumisenestoaine (E 536). Valmistettu vakuumisuolasta lisäämällä jodia kaliumjodidina.), Timjami (Timjami.)",
                                                },
                                                {
                                                    "name": "Creme fraiche",
                                                    "orderNumber": 2,
                                                    "portionSize": 30,
                                                    "diets": "G, L, Mu",
                                                    "ingredients": "Creme fraiche (Pastöroitu KERMA, sakeuttamisaineet (E412. E1442), hapate.) (Maito)",
                                                },
                                                {
                                                    "name": "proteiinilisäke",
                                                    "orderNumber": 3,
                                                    "portionSize": 60,
                                                    "diets": "",
                                                    "ingredients": "***",
                                                },
                                            ],
                                        }
                                    ],
                                }
                            ],
                        }
                    ],
                },
                {
                    "menuTypeId": 82,
                    "menuTypeName": "Foobar Salad and soup",
                    "menus": [
                        {
                            "menuName": "Foobar Salad & Soup (37-42)",
                            "menuAdditionalName": "BI 11.09.2023-20.10.2023",
                            "menuId": 4117,
                            "days": [
                                {
                                    "date": 20230913,
                                    "weekday": 3,
                                    "mealoptions": [
                                        {
                                            "name": "LOUNAS KEITTO",
                                            "orderNumber": 24,
                                            "id": 6,
                                            "menuItems": [
                                                {
                                                    "name": "Punajuurisosekeitto",
                                                    "orderNumber": 1,
                                                    "portionSize": 402,
                                                    "diets": "G, L, Mu, *",
                                                    "ingredients": "Vesi, Punajuuri (karbokuorittu punajuuri (100%)), Peruna (peruna, hapettumisenestoaine (NATRIUMDISULFIITTI)) (Rikkidioksidi), Ruokakerma, Sipuli (sipuli (Puola)), Punajuurikuutio mausteliemessä (Punajuuri, vesi, sokeri, happo (etikkahappo), säilöntäaine (kaliumsorbaatti), neilikka-aromi.), Vähäsuolainen kasvisliemijauhe (Suola, maltodekstriini, sipuli 10 %, luontainen aromi, palsternakka 5,2 %, porkkana 4,6 %, purjo 0,3 %. Kasvikset 20 %.), Suola (Ruokasuola ja paakkuuntumisenestoaine (E 536). Valmistettu vakuumisuolasta lisäämällä jodia kaliumjodidina.), Timjami (Timjami.)",
                                                },
                                                {
                                                    "name": "Creme fraiche",
                                                    "orderNumber": 2,
                                                    "portionSize": 30,
                                                    "diets": "G, L, Mu",
                                                    "ingredients": "Creme fraiche (Pastöroitu KERMA, sakeuttamisaineet (E412. E1442), hapate.) (Maito)",
                                                },
                                                {
                                                    "name": "proteiinilisäke",
                                                    "orderNumber": 3,
                                                    "portionSize": 60,
                                                    "diets": "",
                                                    "ingredients": "***",
                                                },
                                            ],
                                        }
                                    ],
                                }
                            ],
                        }
                    ],
                },
                {
                    "menuTypeId": 83,
                    "menuTypeName": "Foobar Jälkiruoka",
                    "menus": [
                        {
                            "menuName": "Foobar jälkiruoka (37-42)",
                            "menuAdditionalName": "BI 11.09.-20.10.2023",
                            "menuId": 4118,
                            "days": [
                                {
                                    "date": 20230913,
                                    "weekday": 3,
                                    "mealoptions": [
                                        {
                                            "name": "JÄLKIRUOKA",
                                            "orderNumber": 50,
                                            "id": 8,
                                            "menuItems": [
                                                {
                                                    "name": "Kookospannacotta",
                                                    "orderNumber": 1,
                                                    "portionSize": 100,
                                                    "diets": "",
                                                    "ingredients": "Valkoinen leivontasuklaa (Sokeri, kaakaovoi, täysMAITOjauhe, LAKTOOSI, VOIrasva, emulgointiaine (auringonkukkalesitiini, E476), vanilja-aromi. Saattaa sisältää pieniä määriä gluteenia sisältäviä viljoja, soijaa, kananmunaa, pähkinöitä ja maapähkinää.) (maito), Vispikerma (KERMA, stabilointiaine (karrageeni)) (Maito), Kookoskerma (Kookospähkinäuute (90 %), vesi), Tomusokeri (Sokeri ja perunatärkkelys 2%), Mansikka (mansikka (100 %)), Mustikka (pensasmustikka), Liivate (Liivatelehti. Ihmisravinnoksi tarkoitettu gelatiini. Valmistettu sian nahasta.), Valkolupiininverso (suomalainen valkolupiinin verso) (lupiini), Vaniljatanko (Vaniljatanko.)",
                                                }
                                            ],
                                        }
                                    ],
                                }
                            ],
                        }
                    ],
                },
                {
                    "menuTypeId": 84,
                    "menuTypeName": "Foobar Rohee",
                    "menus": [
                        {
                            "menuName": "Ravintola Foobar Rohee (37-42)",
                            "menuAdditionalName": "BI 11.09.2023-20.10.2023",
                            "menuId": 4116,
                            "days": [
                                {
                                    "date": 20230913,
                                    "weekday": 3,
                                    "mealoptions": [
                                        {
                                            "name": "KASVIS OP",
                                            "orderNumber": 7,
                                            "id": 106,
                                            "menuItems": [
                                                {
                                                    "name": "Pinaatti-linssikiusaus",
                                                    "orderNumber": 1,
                                                    "portionSize": 380,
                                                    "diets": "M, Mu, *, VEG",
                                                    "ingredients": "Peruna (Peruna 100%), Kaurajuoma, Vihreä linssi (Liotetut linssit, vesi, suola. Saattaa sisältää pieniä määriä VEHNÄÄ.) (Gluteeni, vehnä), Munakoiso, Kesäkurpitsa (Kesäkurpitsa), Pinaatti, Vaalea kastikeaines (Maissitärkkelys, muunnettu perunatärkkelys, maltodekstriini, suola, kasvisrasvat (palmurasva, karitevoi), emulgointiaine (E 451), hiivauute, muunnettu maissitärkkelys, aromi, väriaine (E 150c), kurkuma, riisijauho.), Vähäsuolainen kasvisliemijauhe (Suola, maltodekstriini, sipuli 10 %, luontainen aromi, palsternakka 5,2 %, porkkana 4,6 %, purjo 0,3 %. Kasvikset 20 %.), Sokeri (sokeri), Suola (Ruokasuola ja paakkuuntumisenestoaine (E 536). Valmistettu vakuumisuolasta lisäämällä jodia kaliumjodidina.), Välimeren yrttimausteseos (Punainen paprika (25%), yrtit (25%)(basilika, oregano, kynteli, timjami), korianteri, valkosipuli, sipuli, maustepippuri.)",
                                                }
                                            ],
                                        },
                                        {
                                            "name": "LOUNAS I",
                                            "orderNumber": 11,
                                            "id": 3,
                                            "menuItems": [
                                                {
                                                    "name": "Broilerpyörykkä",
                                                    "orderNumber": 1,
                                                    "portionSize": 120,
                                                    "diets": "M, Mu, *",
                                                    "ingredients": "Broilerpyörykkä (broilerinliha (50 %), vesi, SOIJAPROTEIINI, koneellisesti eroteltu siipikarjanliha (Suomi), korppujauho (VEHNÄ), mausteet (sipuli, valkopippuri, paprika, mustapippuri, valkosipuli, korianteri, maustepippuri), perunajauho, stabilointiaine auringonkukkalesitiini, dekstroosi, happamuudensäätöaineet (kaliumkloridi, E 300), jodioitu suola, hiivauute, stabilointiaine E 461, aromi. Broilerinlihan alkuperä Suomi) (Gluteeni, Soijapapu, vehnä)",
                                                },
                                                {
                                                    "name": "Vihreä thai-kastike",
                                                    "orderNumber": 2,
                                                    "portionSize": 40,
                                                    "diets": "G, M, Mu, VEG",
                                                    "ingredients": "Vesi, Kookosmaito (kookospähkinäuute (75 %), vesi, emulgointiaine (E471), stabilointiaine (E466).), Vihreä currytahna (Sitruunaruoho, vihreä chili 15 %, vesi, sipuli, valkosipuli, galangal, suola, korianteri, ryppylime, kurkuma.), Vaalea kastikeaines (Maissitärkkelys, muunnettu perunatärkkelys, maltodekstriini, suola, kasvisrasvat (palmurasva, karitevoi), emulgointiaine (E 451), hiivauute, muunnettu maissitärkkelys, aromi, väriaine (E 150c), kurkuma, riisijauho.), Fariinisokeri (Sokeri ja ruokosokerisiirappi), Valkosipulimurska (Valkosipuli 80%, vesi, säilöntäaine: kaliumsorbaatti, stabilointiaine: sitruunahappo.), Maissitärkkelys, Vähäsuolainen kasvisliemijauhe (Suola, maltodekstriini, sipuli 10 %, luontainen aromi, palsternakka 5,2 %, porkkana 4,6 %, purjo 0,3 %. Kasvikset 20 %.), Suola (Ruokasuola ja paakkuuntumisenestoaine (E 536). Valmistettu vakuumisuolasta lisäämällä jodia kaliumjodidina.), Rypsiöljy (rapsiöljy)",
                                                },
                                            ],
                                        },
                                        {
                                            "name": "LOUNAS II",
                                            "orderNumber": 13,
                                            "id": 4,
                                            "menuItems": [
                                                {
                                                    "name": "Pekoninen porsaanlihapata",
                                                    "orderNumber": 1,
                                                    "portionSize": 290,
                                                    "diets": "G, L, M, Mu, *",
                                                    "ingredients": "Vesi, Possunliha kuutio (suomalainen porsaanliha, jodioitu suola.LAKTOOSITON. GLUTEENITON. RUNSASPROTEIININEN.100 g:aan tuotetta käytetty 123 g lihaa.), Porkkana (porkkana), Tomaattisose (tomaatti (100 %, Portugali)), Pekonirouhe (viljaporsaanliha, vesi, jodioitu suola, dekstroosi, stabilointiaine E 450, hapettumisenestoaine E 301, säilöntäaine natriumnitriitti. Viljaporsaanlihan alkuperä Suomi), Sipuli (sipuli (Puola)), Maissitärkkelys, Sokeri (sokeri), Vähäsuolainen lihaliemijauhe (Maltodekstriini, suola, luontainen aromi, naudanlihauute 8,9 %, sipuli.), Rypsiöljy (rapsiöljy), Suola (Ruokasuola ja paakkuuntumisenestoaine (E 536). Valmistettu vakuumisuolasta lisäämällä jodia kaliumjodidina.)",
                                                }
                                            ],
                                        },
                                        {
                                            "name": "LÄMPIMÄT LISUKKEET",
                                            "orderNumber": 71,
                                            "id": 50,
                                            "menuItems": [
                                                {
                                                    "name": "Höyryperunat",
                                                    "orderNumber": 1,
                                                    "portionSize": 20,
                                                    "diets": "G, M, Mu, *, VEG",
                                                    "ingredients": "Peruna (Peruna)",
                                                },
                                                {
                                                    "name": "Tumma pasta",
                                                    "orderNumber": 2,
                                                    "portionSize": 15,
                                                    "diets": "L, M, Mu, *, VEG",
                                                    "ingredients": "Vesi, Täysjyväpasta (TäysjyvädurumVEHNÄ) (Gluteeni, vehnä)",
                                                },
                                                {
                                                    "name": "Täysjyväriisi",
                                                    "orderNumber": 3,
                                                    "portionSize": 15,
                                                    "diets": "G, M, Mu, *, VEG",
                                                    "ingredients": "Vesi, Tummariisi (parboil-käsitelty pitkäjyväinen tumma riisi), Rypsiöljy (rapsiöljy), Suola (Ruokasuola ja paakkuuntumisenestoaine (E 536). Valmistettu vakuumisuolasta lisäämällä jodia kaliumjodidina.)",
                                                },
                                                {
                                                    "name": "Lämmin kasvislisäke",
                                                    "orderNumber": 4,
                                                    "portionSize": 70,
                                                    "diets": "G, VEG",
                                                    "ingredients": "Lämmin kasvislisäke",
                                                },
                                            ],
                                        },
                                    ],
                                }
                            ],
                        }
                    ],
                },
                {
                    "menuTypeId": 85,
                    "menuTypeName": "Foobar Fusion",
                    "menus": [
                        {
                            "menuName": "Foobar Fusion (37-42)",
                            "menuAdditionalName": "BI 11.09.2023-20.10.2023",
                            "menuId": 4120,
                            "days": [
                                {
                                    "date": 20230913,
                                    "weekday": 3,
                                    "mealoptions": [
                                        {
                                            "name": "FUSION",
                                            "orderNumber": 30,
                                            "id": 14,
                                            "menuItems": [
                                                {
                                                    "name": "Tuplajuustoburger",
                                                    "orderNumber": 1,
                                                    "portionSize": 335,
                                                    "diets": "L",
                                                    "ingredients": "Naudan hampurilaispihvi (naudanliha (kasvatettu ja teurastettu: useat EU-maat), suola, pippuri), Hampurilaissämpylä (VEHNÄJAUHO, vesi, sokeri, rypsiöljy, hiiva, SEESAMINSIEMEN, jodioitu suola, emulgointiaine (E472e), säilöntäaine (E282), stabilointiaine (E516), hapettumisenestoaine (E300).) (Gluteeni, Seesaminsiemen, vehnä), Tomaatti (Tomaatti), Cheddarjuusto (CHEDDARJUUSTO (80%, EU ja muu kuin EU), vesi, VOI, sulatesuolat (E331, E339), luontainen JUUSTOaromi, suola, säilöntäaine (E200), värit (E160a, E160c), stabilointiaine (E322 auringonkukkalesitiini).) (Maito), Punasipuli (punasipuli (100 %)), Kevytmajoneesi (vesi, rapsiöljy (EU), muunnettu perunatärkkelys, KANANMUNA, sokeri, SINAPPI (vesi, SINAPINSIEMEN, sokeri, etikka, suola, mausteet), suola, etikka, stabilointiaine (E412), säilöntäaine (E202), happamuudensäätöaineet (E270, E330), väri (E160a)) (Muna, Sinappi), Chilimajoneesi (vesi, rapsiöljy (EU), sokeri, etikka, tomaattisose, muunnettu maissitärkkelys, KANANMUNANKELTUAINEN, jodioitu suola, mausteet (chili, juustokumina, valkosipuli, oregano, cayenne), sakeuttamisaineet (E415, E412), säilöntäaine (E202), paprikauute) (Muna), Jääsalaatti (Jääsalaatti), Vesi, Sokeri (sokeri), Punaviinietikka (punaviinietikka, säilöntäaine (kaliumvetySULFIITTI)) (Rikkidioksidi), Suola (Ruokasuola ja paakkuuntumisenestoaine (E 536). Valmistettu vakuumisuolasta lisäämällä jodia kaliumjodidina.), Mustapippuri (Mustapippuri (Tellicherry Garbled Special Extra Bold).)",
                                                },
                                                {
                                                    "name": "Ranskalaiset perunat",
                                                    "orderNumber": 2,
                                                    "portionSize": 0,
                                                    "diets": "G, M, Mu, VEG",
                                                    "ingredients": "Ranskalaiset perunat (peruna 96% (EU), auringonkukkaöljy)",
                                                },
                                            ],
                                        },
                                        {
                                            "name": "FUSION MEAL",
                                            "orderNumber": 31,
                                            "id": 44,
                                            "menuItems": [
                                                {
                                                    "name": "Vegaaninen Tofu-Guocamoleburger",
                                                    "orderNumber": 1,
                                                    "portionSize": 319,
                                                    "diets": "L, M, *, VEG",
                                                    "ingredients": "Tofu (vesi, SOIJAPAPU 47 %, happamuudensäätöaine (E511)) (Soijapapu), Kaura-spelttihampurilaissämpylä (VEHNÄjauho, vesi, esiliotetut jyvät 11 % (RUIShapantaikina, SPELTIN jyvät), KAURAhiutale 5,9 %, sokeri, rypsiöljy, hiiva, VEHNÄGLUTEENI, VEHNÄrouhe, lesejauhoseos (VEHNÄ), suola, juurisikurikuitu, emulgointiaine (E472e), säilöntäaineet (E282, E202), hapettumisenestoaine (E300). Saattaa sisältää pieniä määriä seesaminsiemeniä.) (Gluteeni, kaura, ruis, Seesaminsiemen, speltti, vehnä), Tomaatti (Tomaatti), Guacamole (Avocado (70%), vesi, punainen paprika, sokeri, suola, valkosipuli, sipuli, hapettumisenestoaineet (E300), sakeuttamisaineet (E401), stabiliointiaineet (E415), jalapeno chili jauhe, happamuudensäätöaineet (E330).), Punasipuli (punasipuli (100 %)), Soijajogurtti (SOIJApohja (vesi, kuorittu SOIJApapu 7,9%), kookosrasva, rapsiöljy, dekstroosi, maissitärkkelys, happamuudensäätöaine (kalsiumsitraatti), sakeuttamisaine (pektiini), suola, hapate. Soijapapujen alkuperä Kanada ja USA.) (Soijapapu), Jääsalaatti (Jääsalaatti), Balsamietikka (viinietikka (Italia), rypälemehutiiviste, väri (E150d). Sisältää SULFIITTEJA.) (Rikkidioksidi), Sokeri (sokeri), Punaviinietikka (punaviinietikka, säilöntäaine (kaliumvetySULFIITTI)) (Rikkidioksidi), Suola (Ruokasuola ja paakkuuntumisenestoaine (E 536). Valmistettu vakuumisuolasta lisäämällä jodia kaliumjodidina.), Rypsiöljy (rapsiöljy)",
                                                },
                                                {
                                                    "name": "Ranskalaiset perunat",
                                                    "orderNumber": 2,
                                                    "portionSize": 0,
                                                    "diets": "G, M, Mu, VEG",
                                                    "ingredients": "Ranskalaiset perunat (peruna 96% (EU), auringonkukkaöljy)",
                                                },
                                            ],
                                        },
                                        {
                                            "name": "FUSION BURGER",
                                            "orderNumber": 32,
                                            "id": 45,
                                            "menuItems": [
                                                {
                                                    "name": "Pohjosen Burger",
                                                    "orderNumber": 1,
                                                    "portionSize": 324,
                                                    "diets": "L",
                                                    "ingredients": "Naudan hampurilaispihvi (naudanliha (kasvatettu ja teurastettu: useat EU-maat), suola, pippuri), Kaura-spelttihampurilaissämpylä (VEHNÄjauho, vesi, esiliotetut jyvät 11 % (RUIShapantaikina, SPELTIN jyvät), KAURAhiutale 5,9 %, sokeri, rypsiöljy, hiiva, VEHNÄGLUTEENI, VEHNÄrouhe, lesejauhoseos (VEHNÄ), suola, juurisikurikuitu, emulgointiaine (E472e), säilöntäaineet (E282, E202), hapettumisenestoaine (E300). Saattaa sisältää pieniä määriä seesaminsiemeniä.) (Gluteeni, kaura, ruis, Seesaminsiemen, speltti, vehnä), Punasipuli (punasipuli (100 %)), Kevytmajoneesi (vesi, rapsiöljy (EU), muunnettu perunatärkkelys, KANANMUNA, sokeri, SINAPPI (vesi, SINAPINSIEMEN, sokeri, etikka, suola, mausteet), suola, etikka, stabilointiaine (E412), säilöntäaine (E202), happamuudensäätöaineet (E270, E330), väri (E160a)) (Muna, Sinappi), Tomaatti (Tomaatti), Savujuustocreme (JUUSTO mm. savuJUUSTO [MAITO, hapate, suola, happamuudensäätöaine (E509), säilöntäaine (E252)], vesi, Laktoositon VOI, sulatesuolat (E452, E339), modifioitu tapiokatärkkelys (E1442), säilöntäaine (E200).) (Maito), Vesi, Savupororouhe (poronliha(60%), saksanhirvenliha(20%), vesi, suola(2,6%), stabilointiaine E451, glukoosi, hapettumisenestoaine E301, luontainen savuaromi, säilöntäaine E250, lihapitoisuus 80%. lihan alkuperämaa: poro; suomi/ ruotsi, saksanhirvenliha; uusiseelanti.), Jääsalaatti (Jääsalaatti), Sokeri (sokeri), Punaviinietikka (punaviinietikka, säilöntäaine (kaliumvetySULFIITTI)) (Rikkidioksidi), Suola (Ruokasuola ja paakkuuntumisenestoaine (E 536). Valmistettu vakuumisuolasta lisäämällä jodia kaliumjodidina.), Mustapippurirouhe (Mustapippuri.)",
                                                },
                                                {
                                                    "name": "Ranskalaiset perunat",
                                                    "orderNumber": 2,
                                                    "portionSize": 200,
                                                    "diets": "G, M, Mu, VEG",
                                                    "ingredients": "Ranskalaiset perunat (peruna 96% (EU), auringonkukkaöljy)",
                                                },
                                            ],
                                        },
                                    ],
                                }
                            ],
                        }
                    ],
                },
                {
                    "menuTypeId": 111,
                    "menuTypeName": "Ravintola Mara",
                    "menus": [
                        {
                            "menuName": "Mara Roheelounas  (37-42)",
                            "menuAdditionalName": "BI 11.09.2023-20.10.2023",
                            "menuId": 4111,
                            "days": [
                                {
                                    "date": 20230913,
                                    "weekday": 3,
                                    "mealoptions": [
                                        {
                                            "name": "KASVIS OP",
                                            "orderNumber": 7,
                                            "id": 106,
                                            "menuItems": [
                                                {
                                                    "name": "Pinaatti-linssikiusaus",
                                                    "orderNumber": 1,
                                                    "portionSize": 380,
                                                    "diets": "M, Mu, *, VEG",
                                                    "ingredients": "Peruna (Peruna 100%), Kaurajuoma, Vihreä linssi (Liotetut linssit, vesi, suola. Saattaa sisältää pieniä määriä VEHNÄÄ.) (Gluteeni, vehnä), Munakoiso, Kesäkurpitsa (Kesäkurpitsa), Pinaatti, Vaalea kastikeaines (Maissitärkkelys, muunnettu perunatärkkelys, maltodekstriini, suola, kasvisrasvat (palmurasva, karitevoi), emulgointiaine (E 451), hiivauute, muunnettu maissitärkkelys, aromi, väriaine (E 150c), kurkuma, riisijauho.), Vähäsuolainen kasvisliemijauhe (Suola, maltodekstriini, sipuli 10 %, luontainen aromi, palsternakka 5,2 %, porkkana 4,6 %, purjo 0,3 %. Kasvikset 20 %.), Sokeri (sokeri), Suola (Ruokasuola ja paakkuuntumisenestoaine (E 536). Valmistettu vakuumisuolasta lisäämällä jodia kaliumjodidina.), Välimeren yrttimausteseos (Punainen paprika (25%), yrtit (25%)(basilika, oregano, kynteli, timjami), korianteri, valkosipuli, sipuli, maustepippuri.)",
                                                }
                                            ],
                                        },
                                        {
                                            "name": "LOUNAS I",
                                            "orderNumber": 11,
                                            "id": 3,
                                            "menuItems": [
                                                {
                                                    "name": "Rapeat kalapalat",
                                                    "orderNumber": 1,
                                                    "portionSize": 150,
                                                    "diets": "M, Mu, *",
                                                    "ingredients": "Rapeat kalapalat (SEITI (64 %)(Pollachius virens, pyydetty troolilla, verkolla, nuotalla sekä koukuilla ja siimoilla Koillis-Atlantilta FAO-alue 27), VEHNÄjauho, rapsiöljy, SEMOLINAVEHNÄ, vesi, perunatärkkelys, maissitärkkelys, suola, VEHNÄGLUTEENI, hiiva, nostatusaineet (E450, E500), sokeri, VEHNÄtärkkelys, pippuriuute) (Gluteeni, Kala, vehnä)",
                                                },
                                                {
                                                    "name": "Lime-tilli-kermaviilikastike",
                                                    "orderNumber": 2,
                                                    "portionSize": 30,
                                                    "diets": "G, L, Mu",
                                                    "ingredients": "Kermaviili (pastöroitu KERMA, hapate) (Maito), Sinappi (Vesi, glukoosi-fruktoosisiirappi, SINAPINSIEMEN (18 %), suola, happamuudensäätöaine (E260), mausteet (sipuli, valkopippuri), säilöntäaine (E211), väri (E150d), paprika-aromi.) (Sinappi), Sokeri (sokeri), Limemehu (Limetäysmehu (99,5%), limeöljy, hapettumisenestoaine (kaliumdiSULFIITTI).) (Rikkidioksidi), Suola (Ruokasuola ja paakkuuntumisenestoaine (E 536). Valmistettu vakuumisuolasta lisäämällä jodia kaliumjodidina.), Tilli (Tilli.), Valkopippuri (Valkopippuri.)",
                                                },
                                            ],
                                        },
                                        {
                                            "name": "LOUNAS II",
                                            "orderNumber": 13,
                                            "id": 4,
                                            "menuItems": [
                                                {
                                                    "name": "Pekoninen porsaanlihapata",
                                                    "orderNumber": 1,
                                                    "portionSize": 300,
                                                    "diets": "G, L, M, Mu, *",
                                                    "ingredients": "Vesi, Possunliha kuutio (suomalainen porsaanliha, jodioitu suola.LAKTOOSITON. GLUTEENITON. RUNSASPROTEIININEN.100 g:aan tuotetta käytetty 123 g lihaa.), Porkkana (porkkana), Tomaattisose (tomaatti (100 %, Portugali)), Pekonirouhe (viljaporsaanliha, vesi, jodioitu suola, dekstroosi, stabilointiaine E 450, hapettumisenestoaine E 301, säilöntäaine natriumnitriitti. Viljaporsaanlihan alkuperä Suomi), Sipuli (sipuli (Puola)), Maissitärkkelys, Sokeri (sokeri), Vähäsuolainen lihaliemijauhe (Maltodekstriini, suola, luontainen aromi, naudanlihauute 8,9 %, sipuli.), Rypsiöljy (rapsiöljy), Suola (Ruokasuola ja paakkuuntumisenestoaine (E 536). Valmistettu vakuumisuolasta lisäämällä jodia kaliumjodidina.)",
                                                }
                                            ],
                                        },
                                        {
                                            "name": "LÄMPIMÄT LISUKKEET",
                                            "orderNumber": 71,
                                            "id": 50,
                                            "menuItems": [
                                                {
                                                    "name": "Höyryperunat",
                                                    "orderNumber": 1,
                                                    "portionSize": 20,
                                                    "diets": "G, M, Mu, *, VEG",
                                                    "ingredients": "Peruna (Peruna)",
                                                },
                                                {
                                                    "name": "Tumma pasta",
                                                    "orderNumber": 2,
                                                    "portionSize": 15,
                                                    "diets": "L, M, Mu, *, VEG",
                                                    "ingredients": "Vesi, Täysjyväpasta (TäysjyvädurumVEHNÄ) (Gluteeni, vehnä)",
                                                },
                                                {
                                                    "name": "Täysjyväriisi",
                                                    "orderNumber": 3,
                                                    "portionSize": 15,
                                                    "diets": "G, M, Mu, *, VEG",
                                                    "ingredients": "Vesi, Tummariisi (parboil-käsitelty pitkäjyväinen tumma riisi), Rypsiöljy (rapsiöljy), Suola (Ruokasuola ja paakkuuntumisenestoaine (E 536). Valmistettu vakuumisuolasta lisäämällä jodia kaliumjodidina.)",
                                                },
                                                {
                                                    "name": "Lämmin kasvislisäke",
                                                    "orderNumber": 4,
                                                    "portionSize": 70,
                                                    "diets": "G, VEG",
                                                    "ingredients": "Lämmin kasvislisäke",
                                                },
                                            ],
                                        },
                                    ],
                                }
                            ],
                        }
                    ],
                },
            ],
        }
    ]
