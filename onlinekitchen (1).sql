-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Дек 06 2021 г., 15:32
-- Версия сервера: 10.4.21-MariaDB
-- Версия PHP: 7.4.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `onlinekitchen`
--

-- --------------------------------------------------------

--
-- Структура таблицы `admins`
--

CREATE TABLE `admins` (
  `id` int(11) NOT NULL,
  `name` text DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `admin_id` int(11) NOT NULL,
  `username` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `admins`
--

INSERT INTO `admins` (`id`, `name`, `phone`, `admin_id`, `username`) VALUES
(5, 'Xamidullo', 998905411173, 1270439555, 'StudentOfTTPU'),
(35, 'Sardor', 999999999, 952552114, 'beshimov_s');

-- --------------------------------------------------------

--
-- Структура таблицы `basket`
--

CREATE TABLE `basket` (
  `id` int(11) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `product_name` text NOT NULL,
  `quantity` bigint(11) NOT NULL,
  `price` bigint(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `basket`
--

INSERT INTO `basket` (`id`, `user_id`, `product_name`, `quantity`, `price`) VALUES
(10, 1185065120, 'Cola', 3, 0),
(11, 1185065120, 'Shashlik - 30000.00 sòm', 3, 0),
(12, 1185065120, 'Mastava - 0.5 \nNarxi - 12000 so\'m', 3, 0);

-- --------------------------------------------------------

--
-- Структура таблицы `drinks`
--

CREATE TABLE `drinks` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `foto_id` text NOT NULL,
  `price` bigint(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `drinks`
--

INSERT INTO `drinks` (`id`, `name`, `foto_id`, `price`) VALUES
(5, 'Cola', 'AgACAgIAAxkBAAITb2GuFLylkeHas09HOxMDA98LMlPvAAJ3ujEb88dwSX3QDpOvjt3kAQADAgADeAADIgQ', 10000);

-- --------------------------------------------------------

--
-- Структура таблицы `fastfood`
--

CREATE TABLE `fastfood` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `foto_id` text NOT NULL,
  `price` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `milliy`
--

CREATE TABLE `milliy` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `foto_id` text NOT NULL,
  `price` bigint(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `milliy`
--

INSERT INTO `milliy` (`id`, `name`, `foto_id`, `price`) VALUES
(7, 'Osh', 'AgACAgIAAxkBAAIWD2GuMDG8MvBl4nuRZMZZOuwX7rGlAAJgvTEbHwVpSZkEEqPO6CjbAQADAgADeAADIgQ', 20000),
(8, 'Sho\'rva', 'AgACAgIAAxkBAAIWFmGuMEU9_40kGKWGtdiDhEuIBzO1AAIRuDEbV0NwSYDS94uqfKKOAQADAgADeQADIgQ', 13000);

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `full_name` text DEFAULT NULL,
  `telegram_id` int(50) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `phone_number` bigint(20) NOT NULL,
  `location` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `full_name`, `telegram_id`, `username`, `phone_number`, `location`) VALUES
(11, '§åřđøř', 934814753, NULL, 998904139920, '3в, Gulsaroy ko\'chasi, Каракамыш, Olmazor Tumani, Toshkent, 100000, Oʻzbekiston'),
(14, 'Xamidullo', 1185065120, 'DataScientist_7', 998330898011, 'Qo`shariq, Andijon, Andijon Tumani, Andijon Viloyati, 170100, Oʻzbekiston'),
(15, 'Sardor', 741898090, 'renamed_1903', 998993061524, '19, Qoraqo\'l ko\'chasi, Заготзерно, Yashnobod Tumani, Toshkent, 100000, Oʻzbekiston'),
(16, '⁪⁬Anjanli', 859464363, 'OYATILLO_Andijoniy', 998995322553, '21, Chuqursoy, Olmazor Tumani, Toshkent, 100000, Oʻzbekiston'),
(17, 's_sultonbekova_', 1985393307, 's_sultonbekova', 998997844096, 'Qo`shariq, Andijon, Andijon Tumani, Andijon Viloyati, 170100, Oʻzbekiston');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `admin_id` (`admin_id`);

--
-- Индексы таблицы `basket`
--
ALTER TABLE `basket`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `drinks`
--
ALTER TABLE `drinks`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `fastfood`
--
ALTER TABLE `fastfood`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `milliy`
--
ALTER TABLE `milliy`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `admins`
--
ALTER TABLE `admins`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=82;

--
-- AUTO_INCREMENT для таблицы `basket`
--
ALTER TABLE `basket`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT для таблицы `drinks`
--
ALTER TABLE `drinks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `fastfood`
--
ALTER TABLE `fastfood`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT для таблицы `milliy`
--
ALTER TABLE `milliy`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
