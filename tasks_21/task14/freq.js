var freq = function(str) {
    var freqs = {};
    n=0
    for(i=0;i<str.length;i++) {
        var txt = str.charAt(i);
        freqs[txt]=(isNaN(freqs[txt]) ? 1 : freqs[txt] + 1);
         }
    return(freqs); 
}
console.log(freq("wwwwerfwdf"));
    
