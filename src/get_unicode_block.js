// src_url: https://en.wikipedia.org/wiki/Unicode_block
// single_row: //*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr
// block_range: /td[2]/span
// block_name: /td[3]/a


function get_block_range(node) {
    return node.getElementsByTagName("td")[1].getElementsByTagName("span")[0].textContent
}
function get_block_name(node) {
    return node.getElementsByTagName("td")[2].getElementsByTagName("a")[0].textContent
}
function get_block_map(nodes) {
    var block_map = Array()
    while (true) {
        var block = nodes.iterateNext()
        if (!block) {
            break
        } else {
            console.log(block)
            block_map.push([get_block_range(block), get_block_name(block)])
        }
    }
    return block_map
}
result = document.evaluate('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[not(@class)]', document)
console.log(get_block_map(result))