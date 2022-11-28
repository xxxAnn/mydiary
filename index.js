function connect(div1, div2, dir) {
    [r1, r2] = [div1.getBoundingClientRect(), div2.getBoundingClientRect()]
    if (dir == 0) {
        var [c1, c2] = [[getCenter(r1), r1.bottom], [getCenter(r2), r2.top]]
    }
    var cn_id = `connect-${div1.id}-${div2.id}`
    let cn = document.getElementById(cn_id) 
    if (cn != null) {
        cn.remove()
    }
    console.log(c1, c2)
    document.body.innerHTML += `
        <svg width="100%" height="100%" class="Blob" id="${cn_id}"><line x1="${c1[0]}" y1="${c1[1]}" x2="${c2[0]}" y2="${c2[1]}" stroke-width=4 stroke="black"/></svg>
    `
}

function getCenter(rect) {
    return (rect.left + rect.right)/2
}

document.body.onload = function(event) {
    //connect(document.getElementById("d1"), document.getElementById("d2"), 0)
}