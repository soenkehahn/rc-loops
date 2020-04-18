#!/usr/bin/env node

for (let i = 0; i < 44100; i++) {
    const random = Math.random() * 2 - 1;
    const volume = 0.05;
    console.log(random * volume)
}
