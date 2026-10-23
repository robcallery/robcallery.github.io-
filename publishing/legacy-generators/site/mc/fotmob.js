// FotMob crest ids (from fotmob.com league tables, Oct 2026): Premier League + Championship
(function () {
  var IDS = {
    manchestercity: 8456, mancity: 8456, arsenal: 9825, brightonandhovealbion: 10204, brighton: 10204,
    brentford: 9937, everton: 8668, chelsea: 8455, leedsunited: 8463, leeds: 8463, hullcity: 8667, hull: 8667,
    liverpool: 8650, ipswichtown: 9902, ipswich: 9902, newcastleunited: 10261, newcastle: 10261,
    crystalpalace: 9826, manchesterunited: 10260, manunited: 10260, manutd: 10260, coventrycity: 8669, coventry: 8669,
    nottinghamforest: 10203, nottmforest: 10203, astonvilla: 10252, sunderland: 8472, bournemouth: 8678,
    tottenhamhotspur: 8586, tottenham: 8586, spurs: 8586, fulham: 9879,
    swanseacity: 10003, swansea: 10003, westhamunited: 8654, westham: 8654, middlesbrough: 8549,
    birminghamcity: 8658, birmingham: 8658, westbromwichalbion: 8659, westbrom: 8659, stokecity: 10194, stoke: 10194,
    wolverhamptonwanderers: 8602, wolves: 8602, wolverhampton: 8602, southampton: 8466,
    queensparkrangers: 10172, qpr: 10172, blackburnrovers: 8655, blackburn: 8655, sheffieldunited: 8657, sheffieldutd: 8657,
    millwall: 10004, portsmouth: 8462, wrexham: 9841, boltonwanderers: 8559, bolton: 8559, bristolcity: 8427,
    charltonathletic: 8451, charlton: 8451, lincolncity: 8430, lincoln: 8430, cardiffcity: 8344, cardiff: 8344,
    watford: 9817, norwichcity: 9850, norwich: 9850, burnley: 8191, derbycounty: 10170, derby: 10170,
    prestonnorthend: 8411, preston: 8411
  };
  var norm = function (s) { return (s || '').toLowerCase().replace(/\b(fc|afc)\b/g, '').replace(/&/g, 'and').replace(/[^a-z0-9]/g, ''); };
  window.fotmobLogo = function (t) {
    if (!t) return '';
    if (String(t.id) === '357') return 'https://images.fotmob.com/image_resources/logo/teamlogo/8463.png';
    var names = [t.displayName, t.name, t.shortDisplayName, t.location, t.nickname];
    for (var i = 0; i < names.length; i++) {
      var id = IDS[norm(names[i])];
      if (id) return 'https://images.fotmob.com/image_resources/logo/teamlogo/' + id + '.png';
    }
    return '';
  };
})();
