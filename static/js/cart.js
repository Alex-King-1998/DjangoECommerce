$(document).on('click', '.add-to-cart-button', function(e) {
    e.preventDefault();  // Prevent the default form submission

    var product_id = $(this).data('product-id');  // Assuming you have data-product-id in your button
    
    $.ajax({
        type: 'POST',
        url: `/product/${product_id}/add-to-cart/`,
        data: {
            csrfmiddlewaretoken: '{{ csrf_token }}',  // Ensure CSRF token is included
        },
        success: function(response) {
            // Update cart count in the UI
            $('#cart-count').text(response.new_cart_count);
            
            // Display success message using a modal or alert
            if (response.success_message) {
                alert(response.success_message);  // Customize this as needed
            }
        },
        error: function(xhr, status, error) {
            // Handle error case
            alert('Error adding item to cart. Please try again.');
        }
    });
});
