
--
-- Indexes for dumped tables
--

--
-- Indexes for table `Fails`
--
ALTER TABLE `Fails`
  ADD PRIMARY KEY (`meal_id`);

--
-- Indexes for table `Locations`
--
ALTER TABLE `Locations`
  ADD PRIMARY KEY (`location_id`);

--
-- Indexes for table `Meals`
--
ALTER TABLE `Meals`
  ADD PRIMARY KEY (`meal_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Fails`
--
ALTER TABLE `Fails`
  MODIFY `meal_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
--
-- AUTO_INCREMENT for table `Locations`
--
ALTER TABLE `Locations`
  MODIFY `location_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `Meals`
--
ALTER TABLE `Meals`
  MODIFY `meal_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81189;