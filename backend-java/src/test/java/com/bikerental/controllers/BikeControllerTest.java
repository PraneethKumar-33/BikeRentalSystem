package com.bikerental.controllers;

import com.bikerental.models.Bike;
import com.bikerental.repositories.BikeRepository;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.web.servlet.MockMvc;

import java.util.Arrays;
import java.util.Optional;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@WebMvcTest(BikeController.class)
public class BikeControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private BikeRepository bikeRepository;

    @Test
    public void testGetAllBikes() throws Exception {
        Bike bike1 = new Bike("Model X", "Sport", 10.0, true);
        Mockito.when(bikeRepository.findAll()).thenReturn(Arrays.asList(bike1));

        mockMvc.perform(get("/api/bikes"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$[0].modelName").value("Model X"));
    }

    @Test
    public void testRentBikeSuccess() throws Exception {
        Bike bike = new Bike("Model Y", "Cruiser", 12.0, true);
        bike.setId(1L);

        Mockito.when(bikeRepository.findById(1L)).thenReturn(Optional.of(bike));

        mockMvc.perform(post("/api/bikes/1/rent"))
                .andExpect(status().isOk())
                .andExpect(content().string("Bike rented successfully!"));
    }
}
