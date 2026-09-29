package com.bikerental.controllers;

import com.bikerental.models.Bike;
import com.bikerental.repositories.BikeRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/bikes")
@CrossOrigin(origins = "*") // Allows Angular frontend to connect
public class BikeController {

    @Autowired
    private BikeRepository bikeRepository;

    @GetMapping
    public List<Bike> getAllBikes() {
        return bikeRepository.findAll();
    }

    @GetMapping("/available")
    public List<Bike> getAvailableBikes() {
        return bikeRepository.findByAvailableTrue();
    }

    @PostMapping("/seed")
    public ResponseEntity<String> seedDatabase() {
        if (bikeRepository.count() == 0) {
            bikeRepository.save(new Bike("Yamaha MT-15", "Sports", 15.0, true));
            bikeRepository.save(new Bike("Honda City", "Cruiser", 12.0, true));
            bikeRepository.save(new Bike("Royal Enfield", "Cruiser", 20.0, false));
            return ResponseEntity.ok("Database seeded!");
        }
        return ResponseEntity.ok("Database already has data.");
    }

    @PostMapping("/{id}/rent")
    public ResponseEntity<String> rentBike(@PathVariable Long id) {
        Optional<Bike> optionalBike = bikeRepository.findById(id);
        if (optionalBike.isPresent()) {
            Bike bike = optionalBike.get();
            if (bike.isAvailable()) {
                bike.setAvailable(false);
                bikeRepository.save(bike);
                return ResponseEntity.ok("Bike rented successfully!");
            } else {
                return ResponseEntity.badRequest().body("Bike is currently unavailable.");
            }
        }
        return ResponseEntity.notFound().build();
    }
}
