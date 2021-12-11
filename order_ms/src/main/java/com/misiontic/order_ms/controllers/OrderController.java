package com.misiontic.order_ms.controllers;

import com.misiontic.order_ms.models.Order;
import com.misiontic.order_ms.repositories.OrderRepository;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@RestController
public class OrderController {

    private final OrderRepository orderRepository;

    public OrderController(OrderRepository orderRepository){
        this.orderRepository = orderRepository;
    }

    @PostMapping("/order")
    Order newOrder(@RequestBody Order order){
        return orderRepository.save(order);
    }

    @GetMapping("/order/{username}")
    List<Order> userOrder(@PathVariable String username){
        List<Order> orderList = orderRepository.findByUsername(username) ;
        return orderList;
    }

    @GetMapping("/orderpost/{username}")
    String prueba(@PathVariable String username){
        return username;
    }

}
