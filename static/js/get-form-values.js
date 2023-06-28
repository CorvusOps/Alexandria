$('.genre-btn').on('click', function (e) {
    var summary = document.getElementById("summary").value;
    var prediction_placeholder = document.getElementById("pred-output");
    e.preventDefault();
    $.ajax({
        type: "GET",
        url: "/predict",
        data: {summary: summary},
        contentType:false,
        cache: false,
        success: function(result) {
         prediction_placeholder.innerHTML = result; 
         console.log(result)
        },
        error: function(event){
          console.log("Cannot produce result. Internal error.")
        }
      });
})