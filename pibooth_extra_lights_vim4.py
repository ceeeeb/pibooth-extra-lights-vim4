# -*- coding: utf-8 -*-

"""Pibooth plugin for extra lights management."""

import pibooth
from pibooth.hardware import LedGroup


__version__ = "1.1.0"


@pibooth.hookimpl
def pibooth_configure(cfg):
    """Declare the new configuration options"""
    cfg.add_option('CONTROLS', 'startup_led_pin', 29,
                   "Physical GPIO OUT pin to light a LED at pibooth startup (list of pins accepted)")
    cfg.add_option('CONTROLS', 'startup_led_active_high', True,
                   "If True, startup LED is lighting by setting pin(s) to HIGH else by setting to LOW")
    cfg.add_option('CONTROLS', 'preview_led_pin', 31,
                   "Physical GPIO OUT pin to light a LED during the entire capture sequence (list of pins accepted)")
    cfg.add_option('CONTROLS', 'preview_led_active_high', True,
                   "If True, preview LED is lighting by setting pin(s) to HIGH else by setting to LOW")
    cfg.add_option('CONTROLS', 'flash_led_pin', 33,
                   "Physical GPIO OUT pin to light a LED when the capture is taken (list of pins accepted)")
    cfg.add_option('CONTROLS', 'flash_led_active_high', True,
                   "If True, flash LED is lighting by setting pin(s) to HIGH else by setting to LOW")


def create_leds(app, cfg, pin_option, active_high_option):
    """Return the group of LEDs declared by the given configuration options.

    Pins are the physical ones of the header: app.board knows which GPIO
    backend the running machine needs.
    """
    active_high = cfg.getboolean('CONTROLS', active_high_option)
    return LedGroup(*(app.board.create_led(pin, active_high)
                      for pin in cfg.gettuple('CONTROLS', pin_option, int)))


@pibooth.hookimpl
def pibooth_startup(app, cfg):
    """Create the LED instances."""
    app.led_startup = create_leds(app, cfg, 'startup_led_pin', 'startup_led_active_high')
    app.led_sequence = create_leds(app, cfg, 'preview_led_pin', 'preview_led_active_high')
    app.led_flash = create_leds(app, cfg, 'flash_led_pin', 'flash_led_active_high')

    # Initial state
    app.led_startup.on()
    app.led_sequence.off()
    app.led_flash.off()


@pibooth.hookimpl
def state_preview_enter(app):
    """Start a new capture sequence."""
    app.led_sequence.on()


@pibooth.hookimpl
def state_capture_enter(app):
    """Ready to take a capture."""
    app.led_flash.on()


@pibooth.hookimpl
def state_capture_exit(app):
    """A capture has been taken."""
    app.led_flash.off()


@pibooth.hookimpl
def state_processing_enter(app):
    """The capture sequence is done."""
    app.led_sequence.off()
