package com.misiontic.order_ms.repositories;
import com.misiontic.order_ms.models.Order;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.List;

public interface OrderRepository extends MongoRepository <Order, String> {
    List<Order> findByUsername (String username);
}
