package com.misiontic.cart_ms.repositories;
import com.misiontic.cart_ms.models.Cart;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.List;

public interface CartRepository extends MongoRepository <Cart, String> {
    List<Cart> findByUsername (String username);
}
