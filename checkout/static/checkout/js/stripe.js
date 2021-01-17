// Stripe code from Code Institute tuturial and Stripe website

let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();
let style = {
    base: {
        color: "#32325d",
        fontFamily: 'Arial, sans-serif',
        fontSmoothing: "antialiased",
        fontSize: "16px",
        "::placeholder": {
            color: "#32325d"
        }
    },
    invalid: {
        fontFamily: 'Arial, sans-serif',
        color: "#fa755a",
        iconColor: "#fa755a"
    }
};
let card = elements.create('card', { style: style });
card.mount('#card-information');

card.addEventListener('change', function (e) {
    let errorDiv = document.getElementbyId('card-errors');
    if (e.error) {
        let html = '<span class="error-message">${e.error.message}</span>';
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

let form = document.getElementById('payment');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({ 'disable': true });
    $('#submit-btn').attr('disable', true);
    stripe.confirmCardPayment(clientSecret, {
       payment_method: {
            card: card,
        }
    }).then(function (result) {
        if (result.error) {
            let errorDiv = document.getElementbyId('card-errors');
            let html = '<span class="result.error-message">${e.error.message}</span>';
            $(errorDiv).html(html);
            card.update({ 'disable': false });
            $('#submit-btn').attr('disable', false);
        }
        else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});