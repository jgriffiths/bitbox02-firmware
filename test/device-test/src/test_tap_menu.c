// Copyright 2019 Shift Cryptosecurity AG
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include <driver_init.h>
#include <firmware_main_loop.h>
#include <screen.h>
#include <string.h>
#include <ui/screen_stack.h>
#include <usb/usb.h>

#include "qtouch.h"
#include "random.h"
#include "util.h"

#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunused-function"

uint32_t __stack_chk_guard = 0;

int main(void)
{
    system_init();
    screen_init();
    qtouch_init();

    // const char* words[] = {"first", "second", "third", "forth"};
    // component_t* test_tap_through = tap_through_create(words, NULL, 4, true);

    // ui_screen_stack_push(test_tap_through);
    firmware_main_loop();
}

#pragma GCC diagnostic pop
