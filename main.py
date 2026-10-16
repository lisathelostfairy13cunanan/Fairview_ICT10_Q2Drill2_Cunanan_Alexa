from pyscript import document

def create_order(*e):
    # clear previous output
    document.getElementById('receipt').innerHTML = " "
    
    # the prices based on ramen nagi menu (only the ramens and gyoza are included)(i got it from the internet)
    menu = {
        "butao": 445.00,
        "black_king": 545.00,
        "red_king": 545.00,
        "green_king": 545.00,
        "gyoza": 180.00,
        "coke": 80.00
    }
    
    subtotal = 0.0
    
    # calculated subtotal based on checked boxes (what they ordered)
    for item_id, price in menu.items():
        checkbox = document.getElementById(item_id)
        if checkbox and checkbox.checked:
            subtotal += price
            
    # calculate the valeu added tax (12%) and total
    vat = subtotal * 0.12
    total = subtotal + vat
    
    # display formatted output matching a receipt style from the example output
    receipt_content = f"""
    <b>==== Receipt ====</b><br><br>
    Subtotal: ₱{subtotal:.2f}<br><br>
    VAT (12%): ₱{vat:.2f}<br><br>
    <b>Total: ₱{total:.2f}</b>
    """
    
    document.getElementById('receipt').innerHTML = receipt_content