package com.misiontic.cart_ms.repositories;
import com.misiontic.cart_ms.models.Order;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface OrdersRepository extends MongoRepository<Order, String> {
}
