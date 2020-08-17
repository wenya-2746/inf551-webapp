$(document).ready( function () {
  $('#data_table').DataTable(
    { language: {
        searchPlaceholder: "Live search records",
        search: "",
      }
    })
} );



// $(document).on('click','button',function(){
//     var table = $(this).parents('table').eq(0);
//     var rows = table.find('tr:gt(0)').toArray().sort(comparer($(this).index()));
//     this.asc = !this.asc;
//     if (!this.asc){rows = rows.reverse();}
//     table.children('tbody').empty().html(rows);
// });

// $(document).on('click','button:first',function(){
//     var table = $(this).parents('table').eq(0);
//     var rows = table.find('tr:gt(0)').toArray().sort(comparer($(this).index()));
//     this.asc = !this.asc;
//     if (!this.asc){rows = rows.reverse();}
//     table.children('tbody').empty().html(rows);
// });
//
// function comparer(index) {
//     return function(a, b) {
//         var valA = getCellValue(a, index), valB = getCellValue(b, index);
//         return $.isNumeric(valA) && $.isNumeric(valB) ?
//             valA - valB : valA.localeCompare(valB);
//     };
// }
// function getCellValue(row, index){
//     return $(row).children('td').eq(index).text();
// }
