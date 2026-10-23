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
    var inkOn = function (bg) { return lum(bg) > .6 ? '#111827' : '#FFFFFF'; };
    var edgeOn = function (bg) { return lum(bg) > .85 ? '#c9ced8' : 'rgba(255,255,255,.92)'; };
    var txt = function (y, fill, size) { return '<text x="50" y="' + y + '" text-anchor="middle" font-family="Barlow Condensed, Arial Narrow, Impact, sans-serif" font-weight="800" font-size="' + (size || 27) + '" letter-spacing="1" fill="' + fill + '">' + code + '</text>'; };
    var shine = '<path d="M0 0 L100 0 L100 18 L0 30 Z" fill="#fff" opacity=".10"/>';
    var style = hash((k || norm(name)) + 'pes') % 5, body = '';
    if (style === 0) {            // classic shield with a band
      var sh = 'M50 4 L90 15 V47 C90 73 72 89 50 97 C28 89 10 73 10 47 V15 Z';
      body = '<defs><clipPath id="c"><path d="' + sh + '"/></clipPath></defs><path d="' + sh + '" fill="' + p + '"/>' +
        '<g clip-path="url(#c)"><rect x="0" y="37" width="100" height="30" fill="' + s + '"/>' + (st ? '<rect x="0" y="67" width="100" height="5" fill="' + st + '"/>' : '') + shine + '</g>' +
        '<path d="' + sh + '" fill="none" stroke="' + edgeOn(p) + '" stroke-width="3.5"/>' + txt(61.5, inkOn(s));
    } else if (style === 1) {     // roundel: coloured ring, plain centre
      body = '<circle cx="50" cy="50" r="46" fill="' + s + '" stroke="' + edgeOn(s) + '" stroke-width="3"/>' +
        '<circle cx="50" cy="50" r="33" fill="' + p + '"/>' + (st ? '<circle cx="50" cy="50" r="33" fill="none" stroke="' + st + '" stroke-width="3"/>' : '') +
        '<circle cx="50" cy="50" r="40" fill="none" stroke="' + inkOn(s) + '" stroke-width="1" stroke-dasharray="2 3" opacity=".7"/>' +
        '<path d="M14 30 A40 40 0 0 1 86 30" fill="#fff" opacity=".08"/>' + txt(59.5, inkOn(p), 26);
    } else if (style === 2) {     // striped circle with a name plate
      var stripes = ''; for (var i = 0; i < 7; i++) stripes += '<rect x="' + (i * 14.3) + '" y="0" width="14.3" height="100" fill="' + (i % 2 ? s : p) + '"/>';
      body = '<defs><clipPath id="c"><circle cx="50" cy="50" r="45"/></clipPath></defs><g clip-path="url(#c)">' + stripes + shine + '</g>' +
        '<circle cx="50" cy="50" r="45" fill="none" stroke="' + edgeOn(p) + '" stroke-width="3.5"/>' +
        '<rect x="16" y="37" width="68" height="27" rx="4" fill="' + (st || p) + '" stroke="' + edgeOn(p) + '" stroke-width="2"/>' + txt(59, inkOn(st || p), 24);
    } else if (style === 3) {     // pointed shield with a diagonal sash
      var sh3 = 'M14 8 H86 V44 C86 70 70 86 50 96 C30 86 14 70 14 44 Z';
      body = '<defs><clipPath id="c"><path d="' + sh3 + '"/></clipPath></defs><path d="' + sh3 + '" fill="' + p + '"/>' +
        '<g clip-path="url(#c)"><path d="M0 70 L100 10 L100 34 L0 94 Z" fill="' + s + '"/>' + (st ? '<path d="M0 94 L100 34 L100 39 L0 99 Z" fill="' + st + '"/>' : '') + shine + '</g>' +
        '<path d="' + sh3 + '" fill="none" stroke="' + edgeOn(p) + '" stroke-width="3.5"/>' +
        '<rect x="22" y="15" width="56" height="25" rx="3" fill="' + p + '" stroke="' + edgeOn(p) + '" stroke-width="1.5"/>' + txt(35.5, inkOn(p), 22);
    } else {                      // half-and-half crest with a crown-like top bar
      var sh4 = 'M12 20 Q12 10 22 10 H78 Q88 10 88 20 V50 C88 74 70 88 50 96 C30 88 12 74 12 50 Z';
      body = '<defs><clipPath id="c"><path d="' + sh4 + '"/></clipPath></defs>' +
        '<g clip-path="url(#c)"><rect x="0" y="0" width="50" height="100" fill="' + p + '"/><rect x="50" y="0" width="50" height="100" fill="' + s + '"/>' +
        '<rect x="0" y="40" width="100" height="26" fill="' + (st || (lum(p) > .5 ? '#111827' : '#FFFFFF')) + '"/>' + shine + '</g>' +
        '<path d="' + sh4 + '" fill="none" stroke="' + edgeOn(p) + '" stroke-width="3.5"/>' +
        '<g fill="' + edgeOn(p) + '"><circle cx="30" cy="5" r="3"/><circle cx="50" cy="3" r="3.5"/><circle cx="70" cy="5" r="3"/></g>' +
        txt(61, inkOn(st || (lum(p) > .5 ? '#111827' : '#FFFFFF')), 24);
    }
    var svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">' + body + '</svg>';
    return (cache[name] = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg));
  };
})();
