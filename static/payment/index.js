var stripe = Stripe('sk_test_51KFusbLG3Rch548FxCBuH88bWsA2kB3OE261rbEtI0FtiHVrGtZCkMAjkjfJwkqlsCzWfQNxDSQmBzEfawCR6bgg00aWEfvbXH')

var elem = document.getElementById('submit');
clientsecret = elem.getAttribute('data-secret');

// Set up Stripe.js and Elements to use in checkout form
var elements = stripe.elements();
var style = {
base: {
    color: "#000",
    lineHeight: '2.4',
    fontSize: '16px'
    }
};

var card = elements.create("card", { style: style });
card.mount("#card-element");

card.on('change', function(event) {
    var displayError = document.getElementById('card-errors')
    if (event.error) {
      displayError.textContent = event.error.message;
      $('#card-errors').addClass('alert alert-info');
    } else {
      displayError.textContent = '';
      $('#card-errors').removeClass('alert alert-info');
    }
});






