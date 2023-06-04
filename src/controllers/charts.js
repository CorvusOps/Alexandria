const fantasy_chart = document.getElementById('fantasyChart');
new Chart(fantasy_chart, {
    type: 'bar',
    data: {
      labels: ['jason',
        'piper',
        'hera',
        'thalia',
        'leo',
        'percy',
        'trio',
        'demigod',
        'aeolus',
        'francisco',
        'zeus',
        'gaea',
        'san',
        'roman',
        'camp',
        'giant',
        'hunter',
        'jackson',
        'coach',
        'fight',
        'hedge',
        'annabeth',
        'aphrodite',
        'shoe',
        'spirit',
        'thanks',
        'rush',
        'goddess',
        'trip',
        'son',
        'wolf',
        'hero',
        'storm',
        'turn',
        'manage',
        'quest',
        'mellie',
        'valdez',
        'mclean',
        'enceladus'
        ],
      datasets: [{
        label: 'TF-IDF Value',
        data: [0.543557269,
            0.297314653,
            0.26498282,
            0.231714776,
            0.176655213,
            0.159699165,
            0.14094262,
            0.139028865,
            0.139028865,
            0.139028865,
            0.139028865,
            0.13249141,
            0.13249141,
            0.119774374,
            0.102653452,
            0.102001826,
            0.099610778,
            0.098828594,
            0.098828594,
            0.095991479,
            0.088327607,
            0.088327607,
            0.088327607,
            0.082184923,
            0.075554375,
            0.071683935,
            0.062501146,
            0.061827714,
            0.060564505,
            0.058672084,
            0.058315984,
            0.058315984,
            0.055906198,
            0.05577595,
            0.052348443,
            0.050369583,
            0.049414297,
            0.049414297,
            0.049414297,
            0.0494142971514545
            ],
        borderWidth: 1
      }]
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

    

const history = document.getElementById('historyChart');
      
        new Chart(history, {
          type: 'bar',
          data: {
            labels: [
            'confidential',
            'american',
            'interrogate',
            'franklin',
            'pack',
            'benjamin',
            'representative',
            'atlantic',
            'tension',
            'rising',
            'secretary',
            'stolen',
            'colony',
            'cross',
            'ordered',
            'state',
            'london',
            'sir',
            'letter',
            'john',
            'one',
        ],
            datasets: [{
              label: '# of Votes',
              data: [0.329876234,
                0.295936941,
                0.28354153,
                0.253818518,
                0.253818518,
                0.243671065,
                0.243671065,
                0.227987247,
                0.224723683,
                0.218767667,
                0.216033613,
                0.210972624,
                0.210972624,
                0.191278291,
                0.188116781,
                0.154621983,
                0.153837972,
                0.148665967,
                0.143974209,
                0.142089481,
                0.083736272,
                ],
              borderWidth: 1
            }]
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
                beginAtZero: true
              }
            }
          }
        });