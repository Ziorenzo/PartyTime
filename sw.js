let cacheName = 'pwa01';

let filesToCache = [

    'index.html',

<<<<<<< HEAD
    'style.css',

    'js/main.js'
=======
    'css/style.css',

    'js/main.js'

>>>>>>> 53ca73be3fe2e709932b56594ce9be6f1de92a9f
];

/* Start the service worker and cache all of the app's content */

self.addEventListener('install', function(e) {

    e.waitUntil(

        caches.open(cacheName).then(function(cache) {

            return cache.addAll(filesToCache);

        })

    );

});

/* Serve cached content when offline */

self.addEventListener('fetch', function(e) {

    e.respondWith(

        caches.match(e.request).then(function(response) {

            return response || fetch(e.request);

        })

    );

});