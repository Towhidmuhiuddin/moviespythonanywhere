$(document).ready(function () {
    $('.increment-btn').click(function (e) { 
        e.preventDefault();
        var inc_value=$(this).closest('.moviedata').find('.qty-input').val();
        var value=parseInt(inc_value,10)
        value=isNaN(value) ? 0 :value;

        if (value<10) {
            value++;
            $(this).closest('.moviedata').find('.qty-input').val(value);
        }
    });
    $('.decrement-btn').click(function (e) { 
        e.preventDefault();
        var dec_value=$(this).closest('.moviedata').find('.qty-input').val();
        var value=parseInt(dec_value,10)
        value=isNaN(value) ? 0 :value;

        if (value>1) {
            value--;
            $(this).closest('.moviedata').find('.qty-input').val(value);
        }
    });

    $('.addToTicket').click(function (e) { 
        e.preventDefault();
        var movie_id=$(this).closest('.moviedata').find('.mov_id').val();
        var ticket_qty=$(this).closest('.moviedata').find('.qty-input').val();
        var token=$('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/add-to-ticket",
            data: {
                'movie_id':movie_id,
                'ticket_qty':ticket_qty,
                csrfmiddlewaretoken:token,
            },
            
            success: function (response) {
                console.log(response);
                alertify.success(response.status);
            }
        });
    });

    $('.changeQuantity').click(function (e) { 
        e.preventDefault();
        var movie_id=$(this).closest('.moviedata').find('.mov_id').val();
        var ticket_qty=$(this).closest('.moviedata').find('.qty-input').val();
        var token=$('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/update-ticket",
            data: {
                'movie_id':movie_id,
                'ticket_qty':ticket_qty,
                csrfmiddlewaretoken:token,
            },
            success: function (response) {
                console.log(response);
                //alertify.success(response.status)
            }
        });
        
    });
    

    $(document).on('click','.delete-ticket-item', function (e) {
        e.preventDefault();
        
        var movie_id=$(this).closest('.moviedata').find('.mov_id').val();
        var token=$('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/delete-ticket",
            data: {
                'movie_id':movie_id,
                csrfmiddlewaretoken : token,
            },
            
            success: function (response) {
                alertify.success(response.status)
                $('.ticketload').load(location.href + " .ticketload")
            }
        });
        
    });

    $('.addtoWishlistBtn').click(function (e) { 
        e.preventDefault();
        var movie_id=$(this).closest('.moviedata').find('.mov_id').val();
        var token=$('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/add-to-wishlist",
            data: {
                'movie_id':movie_id,
                csrfmiddlewaretoken:token,
            },
            
            success: function (response) {
                console.log(response);
                alertify.success(response.status);
            }
        });
    });
    

    $(document).on('click','.delete-wishlist-item', function (e) {
        e.preventDefault();
    
        var movie_id=$(this).closest('.moviedata').find('.mov_id').val();
        var token=$('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/delete-wishlist",
            data: {
                'movie_id':movie_id,
                csrfmiddlewaretoken : token,
            },
            
            success: function (response) {
                alertify.success(response.status)
                $('.wishlistload').load(location.href + " .wishlistload")
            }
        });
    });

});