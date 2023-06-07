/* This javascript file retrieves the csv files of frequent terms 
 * and their relevance value (TF-IDF) per genre
 * and pass these to the charts
 * 
 * NOTE: modify the server link for the files ('http://127.0.0.1:5500') 
 *       when servers changes
 */

// FANTASY FREQUENT TERM CHART

const fantasy_canvas = document.getElementById('fantasyChart');
const fantasyChartData = 'http://127.0.0.1:5500/chart/fantasy-100-tfidf.csv'

d3.csv(fantasyChartData).then(makeChart);

function makeChart(fantasy_tfidf) {

  var fantasy_labels = fantasy_tfidf.map(function(d){
    return d.index;
  });
  var fantasy_books_tfidf = fantasy_tfidf.map(function(d){
    return d.tfidf;
  });

  var chart = new Chart(fantasy_canvas, {
    type: 'bar',
    data: {
      labels: fantasy_labels,
      datasets: [
        {
          label: 'TF-IDF Value',
          data: fantasy_books_tfidf,
          borderWidth: 1
        }
      ]
    }, 
    options: {
      maintainAspectRatio: false,
      plugins: {
          title: {
              display: true,
              text: 'Frequent Terms in Fantasy Books'
          }
      },
    scales: {
      y: {
        beginAtZero: false
      }
    }
  }
  });
}

// HISTORY FREQUENT TERM CHART

const history_canvas = document.getElementById('historyChart');
const historyChartData = 'http://127.0.0.1:5500/chart/history-100-tfidf.csv'

d3.csv(historyChartData).then(makeHistoryChart);

function makeHistoryChart(history_tfidf) {

  var history_labels = history_tfidf.map(function(d){
    return d.index;
  });
  var history_books_tfidf = history_tfidf.map(function(d){
    return d.tfidf;
  });

  const config = {
    type: 'bar',
    data: {
      labels: history_labels,
      datasets: [
        {
          label: 'TF-IDF Value',
          data: history_books_tfidf,
          borderWidth: 1
        }
      ]
    }, 
    options: {
      maintainAspectRatio: false,
      plugins: {
          title: {
              display: true,
              text: 'Frequent Terms in History Books'
          }
      },
    scales: {
      y: {
        beginAtZero: false
      }
    }
  }
  };
  const history_chart = new Chart(
    document.getElementById('historyChart'),
    config
  );
}

// HORROR FREQUENT TERM CHART

const horror_canvas = document.getElementById('horrorChart');
const horrorChartData = 'http://127.0.0.1:5500/chart/horror-100-tfidf.csv'

d3.csv(horrorChartData).then(makeHorrorChart);

function makeHorrorChart(horror_tfidf) {

  var horror_labels = horror_tfidf.map(function(d){
    return d.index;
  });
  var horror_books_tfidf = horror_tfidf.map(function(d){
    return d.tfidf;
  });

  const config = {
    type: 'bar',
    data: {
      labels: horror_labels,
      datasets: [
        {
          label: 'TF-IDF Value',
          data: horror_books_tfidf,
          borderWidth: 1
        }
      ]
    }, 
    options: {
      maintainAspectRatio: false,
      plugins: {
          title: {
              display: true,
              text: 'Frequent Terms in Horror Books'
          }
      },
    scales: {
      y: {
        beginAtZero: false
      }
    }
  }
  };
  const horror_chart = new Chart(
    document.getElementById('horrorChart'),
    config
  );
}

// SCIENCE FREQUENT TERM CHART

const science_canvas = document.getElementById('scienceChart');
const scienceChartData = 'http://127.0.0.1:5500/chart/science-100-tfidf.csv'

d3.csv(scienceChartData).then(makeScienceChart);

function makeScienceChart(science_tfidf) {

  var science_labels = science_tfidf.map(function(d){
    return d.index;
  });
  var science_books_tfidf = science_tfidf.map(function(d){
    return d.tfidf;
  });

  const config = {
    type: 'bar',
    data: {
      labels: science_labels,
      datasets: [
        {
          label: 'TF-IDF Value',
          data: science_books_tfidf,
          borderWidth: 1
        }
      ]
    }, 
    options: {
      maintainAspectRatio: false,
      plugins: {
          title: {
              display: true,
              text: 'Frequent Terms in Science Books'
          }
      },
    scales: {
      y: {
        beginAtZero: false
      }
    }
  }
  };
  const science_chart = new Chart(
    document.getElementById('scienceChart'),
    config
  );
}

// THRILLER FREQUENT TERM CHART

const thriller_canvas = document.getElementById('thrillerChart');
const thrillerChartData = 'http://127.0.0.1:5500/chart/thriller-100-tfidf.csv'

d3.csv(thrillerChartData).then(makeThrillerChart);

function makeThrillerChart(thriller_tfidf) {

  var thriller_labels = thriller_tfidf.map(function(d){
    return d.index;
  });
  var thriller_books_tfidf = thriller_tfidf.map(function(d){
    return d.tfidf;
  });

  const config = {
    type: 'bar',
    data: {
      labels: thriller_labels,
      datasets: [
        {
          label: 'TF-IDF Value',
          data: thriller_books_tfidf,
          borderWidth: 1
        }
      ]
    }, 
    options: {
      maintainAspectRatio: false,
      plugins: {
          title: {
              display: true,
              text: 'Frequent Terms in Thriller Books'
          }
      },
    scales: {
      y: {
        beginAtZero: false
      }
    }
  }
  };
  const thriller_chart = new Chart(
    document.getElementById('thrillerChart'),
    config
  );
}


  

  
