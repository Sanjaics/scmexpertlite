 $(document).ready(function() {
        // Check if the specified item in session storage exists
        if (sessionStorage.getItem("username" ||"email" ||"role") !== null) {
            
           
        } else {
            // Redirect to index.html if the item does not exist
            window.location.href = '../';
        }
    });