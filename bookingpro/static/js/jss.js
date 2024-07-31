document.addEventListener('DOMContentLoaded', (event) => {
    const seats = document.querySelectorAll('.seat.available');
    const selectedSeatsElement = document.getElementById('selected-seats');
    const ticketFareElement = document.getElementById('ticket-fare');

    const seatPrice = 1000; // Price per seat
    let selectedSeatsCount = 0;

    seats.forEach(seat => {
        seat.addEventListener('click', () => {
            if (seat.classList.contains('selected')) {
                seat.classList.remove('selected');
                selectedSeatsCount--;
            } else {
                seat.classList.add('selected');
                selectedSeatsCount++;
            }

            // Update the seat count and fare
            selectedSeatsElement.textContent = selectedSeatsCount;
            ticketFareElement.textContent = `₹ ${selectedSeatsCount * seatPrice}`;
        });
    });
});
// document.addEventListener('DOMContentLoaded', () => {
//     let selectedSeatsCount = 0;

//     // Add event listeners to all "Select Seat" buttons
//     const selectSeatButtons = document.querySelectorAll('.bus-seat-btn');
//     selectSeatButtons.forEach(button => {
//         button.addEventListener('click', () => {
//             const seatContainer = button.parentElement;
//             const busPriceElement = seatContainer.querySelector('.bus-price h2');
//             const selectedSeatsElement = seatContainer.querySelector('.selected-seats');
//             const ticketFareElement = seatContainer.querySelector('.ticket-fare');

//             // Get the price per seat from the bus element
//             const seatPrice = parseInt(busPriceElement.textContent.replace('₹', ''));

//             // Simulating dynamic seat selection
//             selectedSeatsCount++;
//             selectedSeatsElement.textContent = `Selected seats: ${selectedSeatsCount}`;
//             ticketFareElement.textContent = `Total Fare: ₹${selectedSeatsCount * seatPrice}`;
//         });
//     });
// });
