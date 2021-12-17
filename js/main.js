<<<<<<< HEAD

=======
>>>>>>> 53ca73be3fe2e709932b56594ce9be6f1de92a9f
window.onload = () => {

    'use strict';



    if ('serviceWorker' in navigator) {

        navigator.serviceWorker

            .register('./sw.js').then(function (registration) {

                

<<<<<<< HEAD
            // Service worker registered correctly.
=======
            // Service worker registered correctly.​
>>>>>>> 53ca73be3fe2e709932b56594ce9be6f1de92a9f

            console.log('ServiceWorker registration successful with scope: ', registration.scope);

        }, 
<<<<<<< HEAD
        
=======
>>>>>>> 53ca73be3fe2e709932b56594ce9be6f1de92a9f
        function (err) {

            

<<<<<<< HEAD
        // Troubles in registering the service worker. :(
=======
        // Troubles in registering the service worker. :(​
>>>>>>> 53ca73be3fe2e709932b56594ce9be6f1de92a9f

        console.log('ServiceWorker registration failed: ', err);

    });

}

<<<<<<< HEAD
};
=======
}
>>>>>>> 53ca73be3fe2e709932b56594ce9be6f1de92a9f
