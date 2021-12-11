package com.misiontic.cart_ms.controllers;
import com.misiontic.cart_ms.models.Cart;
import com.misiontic.cart_ms.models.Order;
import com.misiontic.cart_ms.repositories.OrdersRepository;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@RestController
public class OrdersController {

    private final OrdersRepository ordersRepository;

    public OrdersController(OrdersRepository ordersRepository){
        this.ordersRepository = ordersRepository;
    }

    @PostMapping("/order")
    Order newOrder(@RequestBody Order order){
        return ordersRepository.save(order);
    }

}
