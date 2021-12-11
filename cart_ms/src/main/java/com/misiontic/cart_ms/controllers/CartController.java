package com.misiontic.cart_ms.controllers;
import com.misiontic.cart_ms.exceptions.AccountNotFoundException;
import com.misiontic.cart_ms.models.Cart;
import com.misiontic.cart_ms.repositories.CartRepository;
import org.springframework.web.bind.annotation.*;
import java.util.List;
import java.util.stream.Collectors;


@RestController
public class CartController {

    private final CartRepository cartRepository;

    public CartController(CartRepository cartRepository) {
        this.cartRepository = cartRepository;
    }

    @GetMapping("/cart/{username}")
    List<Cart> userCart(@PathVariable String username){
        List<Cart> cartList = cartRepository.findByUsername(username);
        return cartList;
    }

    @PostMapping("/cart")
    Cart newCart(@RequestBody Cart cart){
        return cartRepository.save(cart);
    }

    @PutMapping("/cart")
    Cart updateCart(@RequestBody String username, String name, Integer value, Integer newAmount){
        Cart cart = new Cart(username.concat(name),username,name,value,newAmount); /* Por alguna razón queda NULL el newAmount, corregir*/
        List<Cart> user = cartRepository.findByUsername(cart.getUsername());
        Cart objective = (Cart) user.stream().filter(p -> p.getName() == cart.getName()); /* Esta parte no funciona, toca corregirla */
        cartRepository.deleteById(objective.getId());
        return cartRepository.save(cart);
    }

    @DeleteMapping("/cart")
    void deleteCart(@RequestBody String username, String name, Integer value, Integer amount){
        Cart cart = new Cart(username.concat(name),username,name,value,amount);
        List<Cart> user = cartRepository.findByUsername(cart.getUsername());
        Cart objective = (Cart) user.stream().filter(p -> p.getName() == cart.getName()); /* No funciona */
        cartRepository.deleteById(objective.getId());
    }


}
