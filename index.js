function connect(div1, div2) {
    [r1, r2] = [div1.getBoundingClientRect(), div2.getBoundingClientRect()]
    var [c1, c2] = [[getCenter(r1), getVCenter(r1)], [getCenter(r2), getVCenter(r2)]]
    var cn_id = `connect-${div1.id}-${div2.id}`
    let cn = document.getElementById(cn_id) 
    if (cn != null) {
        cn.remove()
    }
    console.log(c1, c2)
    document.body.innerHTML += `
        <svg width="100" height="100" class="line" id="${cn_id}"><line x1="${c1[0]}" y1="${c1[1]}" x2="${c2[0]}" y2="${c2[1]}" stroke-width=4 stroke="black"/></svg>
    `
}

function getCenter(rect) {
    return (rect.left + rect.right)/2
}

function getVCenter(rect) {
    return (rect.top + rect.bottom)/2
}

var LOGS = {}

document.body.onload = function(event) {
    t = document.getElementById("thething")
    t.innerHTML = ""
    Object.keys(LOGS).forEach(x => t.innerHTML += `
        <li><div class="blob" id="${x}" onmouseenter="
            document.getElementById('${x}').innerHTML = \`${LOGS[x]}\`
        " onmouseleave="
            document.getElementById('${x}').innerHTML = '${x}'
        ">${x}</div></li>
    `)
}