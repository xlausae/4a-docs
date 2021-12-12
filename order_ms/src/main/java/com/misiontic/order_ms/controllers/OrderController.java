package com.misiontic.order_ms.controllers;

import org.springframework.web.bind.annotation.*;
import com.misiontic.order_ms.models.Order;
import com.misiontic.order_ms.repositories.OrderRepository;
import java.util.Date;
import java.util.List;

@RestController
public class OrderController {

    private final OrderRepository orderRepository;

    public OrderController(OrderRepository orderRepository) {
        this.orderRepository = orderRepository;
    }

    @PostMapping("/orders")
    Order newOrder(@RequestBody Order order) {
        order.setDate(new Date());
        return orderRepository.save(order);
    }

    @GetMapping("/orders/{username}")
    List<Order> userOrder(@PathVariable String username) {
        return orderRepository.findByUsername(username);

    }

}
