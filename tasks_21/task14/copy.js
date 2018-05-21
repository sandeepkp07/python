var freq = function(str) {
    var freqs = {};
    n=0
    for(i=0;i<str.length;i++) {
        var txt = str.charAt(i);
        freqs[txt]=(isNaN(freqs[txt]) ? 1 : freqs[txt] + 1);
         }
    var list = Object.keys(freqs).map(function(key){
        return [key,freqs[key]];
});
    list.sort(function(first, second) {
        return second[1] - first[1];
});
    console.log(list);
 }    

console.log(freq("wwwwerfwdf"));
    
