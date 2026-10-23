/* Our own team markers: a plain shield in the club's colours with a three-letter code.
   No club crests are used anywhere on this page. */
(function () {
  // [shield, band, stripe] - club colours only
  var C = {
    arsenal: ['#EF0107', '#FFFFFF'], astonvilla: ['#670E36', '#95BFE5'], bournemouth: ['#DA291C', '#111111'],
    brentford: ['#E30613', '#FFFFFF'], brighton: ['#0057B8', '#FFFFFF'], burnley: ['#6C1D45', '#99D6EA'],
    chelsea: ['#034694', '#FFFFFF'], crystalpalace: ['#1B458F', '#C4122E'], everton: ['#003399', '#FFFFFF'],
    fulham: ['#FFFFFF', '#111111'], leedsunited: ['#FFFFFF', '#1D428A', '#FFCD00'], liverpool: ['#C8102E', '#F6EB61'],
    manchestercity: ['#6CABDD', '#FFFFFF', '#1C2C5B'], manchesterunited: ['#DA291C', '#FBE122', '#111111'], newcastle: ['#241F20', '#FFFFFF'],
    nottingham: ['#DD0000', '#FFFFFF'], sunderland: ['#EB172B', '#FFFFFF'], tottenham: ['#132257', '#FFFFFF'],
    westham: ['#7A263A', '#1BB1E7'], wolverhampton: ['#FDB913', '#231F20'], coventry: ['#5BB3E6', '#FFFFFF'],
    ipswich: ['#0044AA', '#FFFFFF'], southampton: ['#D71920', '#FFFFFF'], leicester: ['#003090', '#FDBE11'],
    sheffieldunited: ['#EE2737', '#111111'], sheffieldwednesday: ['#0E5BB5', '#FFFFFF', '#FFCD00'], middlesbrough: ['#E11B22', '#FFFFFF'],
    norwich: ['#FFF200', '#00A650'], westbromwich: ['#122F67', '#FFFFFF'], stoke: ['#E03A3E', '#FFFFFF'], hull: ['#F5A12D', '#111111'],
    derby: ['#FFFFFF', '#111111'], millwall: ['#001D5E', '#FFFFFF'], queensparkrangers: ['#1D5BA4', '#FFFFFF'], swansea: ['#FFFFFF', '#111111'],
    watford: ['#FBEE23', '#ED2127', '#111111'], bristolcity: ['#E21F26', '#FFFFFF'], preston: ['#FFFFFF', '#001E50'], blackburn: ['#009EE0', '#FFFFFF'],
    portsmouth: ['#001489', '#FFFFFF'], oxfordunited: ['#FFE100', '#00205B'], charlton: ['#D4021D', '#FFFFFF'], wrexham: ['#D71920', '#FFFFFF'],
    birmingham: ['#0000CC', '#FFFFFF'], cardiff: ['#0070B5', '#FFFFFF'], plymouth: ['#00513A', '#FFFFFF'], luton: ['#F78F1E', '#002D62'],
    bradford: ['#7A1E2E', '#F9B000'], huddersfield: ['#0E63AD', '#FFFFFF'], barnsley: ['#D71920', '#FFFFFF'], rotherham: ['#D71920', '#FFFFFF']
  };
  var CODE = { leedsunited: 'LEE', manchestercity: 'MCI', manchesterunited: 'MUN', nottingham: 'NFO', tottenham: 'TOT', westham: 'WHU',
    wolverhampton: 'WOL', crystalpalace: 'CRY', astonvilla: 'AVL', sheffieldunited: 'SHU', sheffieldwednesday: 'SHW', westbromwich: 'WBA',
    queensparkrangers: 'QPR', bristolcity: 'BRC', newcastle: 'NEW', brighton: 'BHA', bournemouth: 'BOU', brentford: 'BRE', southampton: 'SOU' };
  var norm = function (s) { return String(s || '').toLowerCase().replace(/&/g, 'and').replace(/[^a-z]/g, ''); };
  function keyOf(name) { var n = norm(name); for (var k in C) if (n.indexOf(k) >= 0) return k; return null; }
  function lum(hex) { var h = hex.replace('#', ''); if (h.length === 3) h = h.replace(/./g, '$&$&');
    var r = parseInt(h.slice(0, 2), 16), g = parseInt(h.slice(2, 4), 16), b = parseInt(h.slice(4, 6), 16); return (0.299 * r + 0.587 * g + 0.114 * b) / 255; }
  var PAL = [['#1E3F9A', '#FFFFFF'], ['#7A1F2B', '#F3E2B8'], ['#0F6F73', '#FFFFFF'], ['#3A3F4B', '#FFCD00'], ['#2F6B3C', '#FFFFFF'], ['#6B2FA3', '#FFFFFF']];
  function hash(s) { var h = 0; for (var i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) >>> 0; return h; }
  var cache = {};
  window.teamMarker = function (t) {
    t = t || {};
    var name = t.displayName || t.name || t.shortDisplayName || t.location || '';
    if (cache[name]) return cache[name];
    var k = keyOf(name), cols = k ? C[k] : null;
    if (!cols) {
      var a = t.color && /^[0-9a-f]{6}$/i.test(t.color) ? '#' + t.color : null, b = t.alternateColor && /^[0-9a-f]{6}$/i.test(t.alternateColor) ? '#' + t.alternateColor : null;
      cols = a && b && a.toLowerCase() !== b.toLowerCase() ? [a, b] : PAL[hash(name) % PAL.length];
    }
    var code = (k && CODE[k]) || String(t.abbreviation || '').toUpperCase().replace(/[^A-Z]/g, '').slice(0, 3) ||
      norm(String(name).replace(/\b(fc|afc|city|town|united|athletic|rovers|county)\b/gi, '')).slice(0, 3).toUpperCase() || '???';
    var p = cols[0], s = cols[1], st = cols[2] || (lum(p) > .8 && lum(s) > .8 ? '#1E3F9A' : null);
    var ink = lum(s) > .6 ? '#111827' : '#FFFFFF', edge = lum(p) > .85 ? '#c9ced8' : 'rgba(255,255,255,.9)';
    var shield = 'M50 4 L90 15 V47 C90 73 72 89 50 97 C28 89 10 73 10 47 V15 Z';
    var svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><clipPath id="c"><path d="' + shield + '"/></clipPath></defs>' +
      '<path d="' + shield + '" fill="' + p + '"/>' +
      '<g clip-path="url(#c)"><rect x="0" y="37" width="100" height="30" fill="' + s + '"/>' + (st ? '<rect x="0" y="67" width="100" height="5" fill="' + st + '"/>' : '') +
      '<path d="M0 0 L100 0 L100 18 L0 30 Z" fill="#fff" opacity=".10"/></g>' +
      '<path d="' + shield + '" fill="none" stroke="' + edge + '" stroke-width="3.5"/>' +
      '<text x="50" y="61.5" text-anchor="middle" font-family="Barlow Condensed, Arial Narrow, Impact, sans-serif" font-weight="800" font-size="27" letter-spacing="1" fill="' + ink + '">' + code + '</text></svg>';
    return (cache[name] = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg));
  };
})();
