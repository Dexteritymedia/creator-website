const CACHE_NAME = 'my-pwa-cache-v1';
const urlsToCache = [
  '/',
  '/static/src/style.css',
  '/static/src/output.css',
  '/static/src/style.js',
  //'/static/js/scripts.js', make sure the urls here does not return a 404 error not found
  '/static/icons/icon-192x192.png',
  '/static/icons/icon-512x512.png',
];

// Install the service worker
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(urlsToCache);
    })
  );
});

// Fetch resources
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      return response || fetch(event.request);
    })
  );
});

// Activate and clean up old caches
self.addEventListener('activate', event => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (!cacheWhitelist.includes(cacheName)) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});