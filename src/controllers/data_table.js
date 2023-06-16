/* This javascript file retrieves the json files 
 * about the books and display the information
 * to the data table
 * 
 * NOTE: modify the data columns name when retrieving from a 
 * different json file
 */

$(document).ready(function () {
    $('#tableID').dataTable({
        "ajax": "../../sample-data.json",
        "columns": [
            { 'data': 'index' },
            { 'data': 'title' },
            { 'data': 'genre' },
            { 'data': 'summary' }
        ]
    });
});